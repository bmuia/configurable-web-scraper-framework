# scraper/cli.py
import argparse
from rich.console import Console
from rich.panel import Panel
from scraper.pipeline import run_pipeline

console = Console()

def main():
    console.print(Panel.fit(
        "[bold cyan]🚀 Configurable Web Scraper Framework CLI 🚀[/bold cyan]\n"
        "[green]Fast • Modular • Export-ready[/green]"
    ))
    parser = argparse.ArgumentParser(description="Belam Web Scraper CLI")
    subparsers = parser.add_subparsers(dest="command")

    # Run subcommand
    run_scraper = subparsers.add_parser("run", help="Run all scrapers")
    run_scraper.add_argument(
        "--verbose", "-v", action="store_true", help="Print detailed results"
    )

    args = parser.parse_args()

    if args.command == "run":
        console.print("[bold blue]ℹ INFO:[/bold blue] Starting scraping...")
        results = run_pipeline()

        if args.verbose:
            console.print(results)
        console.print("[bold green]✅ SUCCESS:[/bold green] Scraping completed!")

    else:
        parser.print_help()
