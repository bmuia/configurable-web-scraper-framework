from scraper.fetcher import fetch_url
from scraper.parser import parse_scraper

class WebScraper:
    """
    A generic web scraper that fetches a page and parses multiple fields
    from a container using CSS selectors, fully driven by YAML configuration.
    """

    def __init__(self, url, item_container_selector, fields, max_attempts=5, back_off=2):
        self.url = url
        self.item_container_selector = item_container_selector
        self.fields = fields
        self.max_attempts = max_attempts
        self.back_off = back_off

    def run(self):
        # Fetch HTML content
        response = fetch_url(
            url=self.url,
            max_attempts=self.max_attempts,
            back_off=self.back_off
        )

        # Parse all fields at once
        results = parse_scraper(
            response,
            item_container_selector=self.item_container_selector,
            fields=self.fields
        )

        return results
