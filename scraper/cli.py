# scraper/cli.py
import argparse
from scraper.pipeline import run_pipeline

def main():
    parser = argparse.ArgumentParser(description="Belam Web Scraper CLI")
    subparsers = parser.add_subparsers(dest="command")

    # Run subcommand
    run_parser = subparsers.add_parser("run", help="Run all scrapers")

    args = parser.parse_args()

    if args.command == "run":
        print("[INFO] Starting scraping...")
        results = run_pipeline()
        print("[INFO] Scraping completed!")
        print(results)
    else:
        parser.print_help()
