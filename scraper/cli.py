import os
import argparse
from scraper.framework import run_pipeline
from scraper.pipeline import save_as_json, save_as_csv



def main():
    parser = argparse.ArgumentParser(description="Run the web scraper CLI")

    parser.add_argument("--format", choices=["json", "csv"], default="json",
                        help="Output format (default: json)")
    parser.add_argument("--output", default="output",
                        help="Output directory (default: ./output)")
    parser.add_argument("--verbose", action="store_true",
                        help="Enable debug logs")

    args = parser.parse_args()

    os.makedirs(args.output, exist_ok=True)

    all_results = run_pipeline()

    for url, results in all_results.items():
        if not results:
            print(f"[WARN] No results scraped from {url}")
            continue

        filename = os.path.join(
            args.output,
            f"{url.replace('https://','').replace('/','_')}.{args.format}"
        )

        if args.format == "json":
            save_as_json(results, filename)
        elif args.format == "csv":
            save_as_csv(results, filename)

        if args.verbose:
            print(f"[INFO] Saved {len(results)} items → {filename}")


if __name__ == "__main__":
    main()
