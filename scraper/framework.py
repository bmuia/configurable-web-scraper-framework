from scraper.fetcher import fetch_url
from config.config_utils import fetch_configuration_details

class WebScraper:
    def __init__(self, url, max_attempts=5, back_off=2):
        self.url = url
        self.max_attempts = max_attempts
        self.back_off = back_off

    def run(self):
        """
        Run the scraper for this site.
        """
        fetch_url(
            url=self.url,
            max_attempts=self.max_attempts,
            back_off=self.back_off
        )
        

if __name__ == '__main__':
    sites = fetch_configuration_details()

    for site in sites:
        url = site["url"]
        max_attempts = site["max_attempts"]
        back_off = site["back_off"]

        scraper = WebScraper(url, max_attempts, back_off)
        scraper.run()
