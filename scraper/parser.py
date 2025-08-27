from bs4 import BeautifulSoup
from rich.console import Console

console = Console()

def parse_scraper(response, item_container_selector, fields):
    """
    Parse HTML response and extract data based on container and fields.

    :param response: requests.Response object
    :param item_container_selector: CSS selector for main item container
    :param fields: list of dicts, e.g. [{'name': ..., 'selector': ..., 'attribute': 'text'}, ...]
    :return: list of dicts with extracted data
    """
    try:
        soup = BeautifulSoup(response.content, 'html.parser')
        results = []

        containers = soup.select(item_container_selector)
        for container in containers:
            item = {}
            for field in fields:
                name = field['name']
                selector = field['selector']

                element = container.select_one(selector)
                if element:
                    item[name] = element.get_text(strip=True)

                else:
                    console.print(
                        f"[bold red]❌ ERROR:[/bold red] "
                        f"Selector '[cyan]{selector}[/cyan]' not found for field '[yellow]{name}[/yellow]'"
                    )

            if item: 
                results.append(item)

        return results

    except Exception as e:
        console.print(f"[bold red]❌ ERROR:[/bold red] Failed to parse scraper: [white]{e}[/white]")
        return []
