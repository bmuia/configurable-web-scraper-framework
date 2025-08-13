import requests
from bs4 import BeautifulSoup
import os
import csv
import json
import math

class EcommerceScraper:
    def __init__(self, url):
        self.url = url
        self.all_products = []
        self.page_size = 10

    def fetch_page(self):
        self.page = requests.get(self.url)
        if self.page.status_code == 200:
            print("Successfully fetched the page")
            return True
        else:
            print("Failed to fetch the page")
            return False

    def parse_page(self):
        self.soup = BeautifulSoup(self.page.content, 'html.parser')
        self.products = self.soup.select('div.product-wrapper.card-body')

    def extract_products(self):
        for product in self.products:
            link_tag = product.select_one('a.title')
            title = link_tag['title'] if link_tag else "No title found"

            price_tag = product.select_one('span[itemprop="price"]')
            price = price_tag.text.strip() if price_tag else "No price found"

            desc_tag = product.select_one('p.description')
            description = desc_tag.text.strip() if desc_tag else "No description found"

            review_tag = product.select_one('p.review-count span')
            reviews = review_tag.text.strip() if review_tag else "0"

            ratings = product.select('span.ws-icon-star')
            stars = len(ratings)

            self.all_products.append({
                'title': title,
                'price': price,
                'description': description,
                'reviews': reviews,
                'stars': stars
            })

    def paginate_data(self, pg=1):
        total_products = len(self.all_products)
        total_pages = math.ceil(total_products / self.page_size)

        current_page = pg
        next_page = pg + 1 if current_page < total_pages else None
        previous_page = pg - 1 if current_page > 1 else None

        start_index = (pg - 1) * self.page_size
        end_index = start_index + self.page_size
        paginated_data = self.all_products[start_index:end_index]

        return paginated_data, current_page, next_page, previous_page

    def save_csv(self, data, filename='output/ecommerce.csv'):
        os.makedirs('output', exist_ok=True)
        with open(filename, 'w', newline='') as output_file:
            fields = ['title', 'price','description','reviews','stars']
            csvwriter = csv.DictWriter(output_file, fieldnames=fields)
            csvwriter.writeheader()
            for p in data:
                csvwriter.writerow(p)
        print(f"Saved CSV to {filename}")

    def save_json(self, data, filename='json/ecommerce.json'):
        os.makedirs('json', exist_ok=True)
        with open(filename, 'w') as output_file:
            json.dump(data, output_file, indent=2)
        print(f"Saved JSON to {filename}")

    def run(self, page_number=1):
        if self.fetch_page():
            self.parse_page()
            self.extract_products()
            page_data, current, next_page, prev_page = self.paginate_data(pg=page_number)
            self.save_csv(page_data)
            self.save_json(page_data)
            print(f"Scraped {len(self.all_products)} total products from {self.url}")
            print(f"Showing page {current} | Previous: {prev_page} | Next: {next_page}")

# Usage example
scraper = EcommerceScraper('https://webscraper.io/test-sites/e-commerce/allinone/computers/laptops')
scraper.run(page_number=2) 
