from bs4 import BeautifulSoup

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
                    print(f"[ERROR] Selector '{selector}' not found for field '{name}'")

            if item: 
                results.append(item)

        return results

    except Exception as e:
        print(f"[ERROR] Failed to parse scraper: {e}")
        return []
