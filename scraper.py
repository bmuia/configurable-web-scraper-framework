import requests
from bs4 import BeautifulSoup
import csv
import os


page = requests.get("https://books.toscrape.com/")
page.raise_for_status() 


soup = BeautifulSoup(page.content, 'html.parser')


products = soup.select('article.product_pod')

all_products = []

for prod in products:
    link_tag = prod.select_one('h3 a')
    link_title = link_tag['title'] if link_tag else 'No title found'

    price_tag = prod.select_one('p.price_color')
    item_price = price_tag.text if price_tag else 'No price found'

    info = {
        'title': link_title,
        'price': item_price,
    }

    all_products.append(info)


os.makedirs('output', exist_ok=True)  
filename = 'output/products.csv'

with open(filename, 'w', newline='', encoding='utf-8') as output_file:
    fields = ['title', 'price']
    csvwriter = csv.DictWriter(output_file, fieldnames=fields)
    csvwriter.writeheader() 

    for product in all_products:
        csvwriter.writerow(product)

print(f"Scraped {len(all_products)} products and saved to {filename}")
