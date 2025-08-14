import requests
from bs4 import BeautifulSoup
import typer
from rich.table import Table
from rich.console import Console
from rich.progress import Progress
from typing_extensions import Annotated
import math
import time

console = Console()

class WebScraper:
    def __init__(self, url: str, page: int = 1):
        self.url = url
        self.page = page
        self.products = []

    def fetch(self):
        response = requests.get(self.url)
        if response.status_code != 200:
            console.print(f"[red]Error: {response.status_code}[/red]")
            raise typer.Exit()
        self.soup = BeautifulSoup(response.content, 'html.parser')

    def scrape_products(self):
        items = self.soup.select('article.product_pod')
        page_size = 10
        total_pages = math.ceil(len(items) / page_size)
        current_page = max(1, min(self.page, total_pages))
        start_index = (current_page - 1) * page_size
        end_index = min(start_index + page_size, len(items))
        paginated = items[start_index:end_index]

        table = Table(
            title=f"[bold magenta]📦 Scraped Products - Page {current_page}/{total_pages}[/bold magenta]",
            title_style="bold magenta",
            header_style="bold cyan",
            border_style="bright_blue",
            show_lines=True
        )
        table.add_column("Title", style="yellow", no_wrap=True)
        table.add_column("Price", style="green")
        table.add_column("Stock", style="bold")

        with Progress() as progress:
            task = progress.add_task("[cyan]Scraping products...", total=len(paginated))
            for p in paginated:
                title = p.select_one('h3 a')['title'] if p.select_one('h3 a') else "No title found"
                price = p.select_one('p.price_color').text.strip() if p.select_one('p.price_color') else "No price found"
                stock = p.select_one('p.instock.availability').text.strip() if p.select_one('p.instock.availability') else "Unknown"
                stock_style = "green" if "In stock" in stock else "red"
                table.add_row(title, price, f"[{stock_style}]{stock}[/{stock_style}]")
                self.products.append({'title': title, 'price': price, 'stock': stock})
                time.sleep(0.3)
                progress.update(task, advance=1)
        console.print(table)


def main(
    url: Annotated[str, typer.Argument(help="Website URL to scrape")],
    page: Annotated[int, typer.Argument(help="Page number to view")] = 1
):
    scraper = WebScraper(url, page)
    scraper.fetch()
    scraper.scrape_products()


if __name__ == "__main__":
    typer.run(main)
