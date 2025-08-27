from scraper.framework import WebScraper
from config.config_utils import open_configuration_file
from scraper.data_exporter import save_file_results
from rich.console import Console

console = Console()

def run_pipeline():
    """Run all scrapers from YAML configuration and return results."""
    configuration = open_configuration_file()
    scrapers_config = configuration.get('scrapers', [])
    all_results = {}

    for scraper_conf in scrapers_config:
        scraper = WebScraper(
            url=scraper_conf['base_url'],
            item_container_selector=scraper_conf['item_container_selector'],
            fields=scraper_conf['fields'],
            max_attempts=scraper_conf.get('max_retries', 5),
            back_off=scraper_conf.get('back_off', 2)
        )

        try:
            results = scraper.run()
            all_results[scraper_conf['name']] = results

            console.print(
                f"[bold blue]ℹ INFO:[/bold blue] Scraped [yellow]{scraper_conf['name']}[/yellow] → "
                f"[green]{len(results)}[/green] items"
            )

            output_config = scraper_conf.get('output')
            if output_config:
                save_file_results(results, output_config)
                console.print(
                    f"[bold green]✅ SUCCESS:[/bold green] Results saved for [yellow]{scraper_conf['name']}[/yellow]"
                )

        except Exception as e:
            console.print(
                f"[bold red]❌ ERROR:[/bold red] Failed to scrape [yellow]{scraper_conf['name']}[/yellow] → {e}"
            )

    return all_results
