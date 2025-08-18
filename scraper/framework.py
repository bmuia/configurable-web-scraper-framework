from scraper.fetcher import fetch_url
from scraper.parser import parse_scraper
from config.config_utils import fetch_configuration_details


class WebScraper:
    def __init__(self, url, container_selector, selectors, max_attempts=5, back_off=2):
        self.url = url
        self.max_attempts = max_attempts
        self.back_off = back_off
        self.container_selector = container_selector
        self.selectors = selectors

    def run(self):
        response = fetch_url(
            url=self.url,
            max_attempts=self.max_attempts,
            back_off=self.back_off
        )
        return parse_scraper(
            response,
            container_selector=self.container_selector,
            selectors=self.selectors,
        )


def run_pipeline():
    """Run scraper for all sites from config and return results."""
    sites = fetch_configuration_details()
    all_results = {}

    for site in sites:
        scraper = WebScraper(
            url=site["url"],
            container_selector=site["container_selector"],
            selectors=site["selectors"],
            max_attempts=site.get("max_attempts", 5),
            back_off=site.get("back_off", 2)
        )
        results = scraper.run()
        all_results[site["url"]] = results
        print(f"[INFO] Scraped {site['url']} → {len(results)} items")
    return all_results


if __name__ == '__main__':
    run_pipeline()
