import os
import json
import csv
from datetime import datetime
from rich.console import Console

console = Console()

def save_file_results(data, output_config):
    """
    Save scraped data to a file based on output configuration.

    :param data: List of dictionaries containing scraped items
    :param output_config: Dict with 'type' (json/csv) and optional 'path'
    """
    output_type = output_config.get("type", "json").lower()
    path = output_config.get("path", "data/output.json")
    os.makedirs(os.path.dirname(path), exist_ok=True)

    timestamp = datetime.now().isoformat(timespec="seconds")

    try:
        if output_type == "json":
            with open(path, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=4)

        elif output_type == "csv":
            if len(data) == 0:
                console.print(f"[{timestamp}] ⚠ [bold yellow]WARNING:[/bold yellow] No data to save for CSV at {path}")
                return

            keys = data[0].keys()
            with open(path, 'w', newline='', encoding='utf-8') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=keys)
                writer.writeheader()
                writer.writerows(data)

        else:
            console.print(f"[{timestamp}] ⚠ [bold yellow]WARNING:[/bold yellow] Unsupported output type: [cyan]{output_type}[/cyan]")
            return

        console.print(f"[{timestamp}] ✅ [bold green]SUCCESS:[/bold green] Data saved to [cyan]{path}[/cyan]")

    except Exception as e:
        console.print(f"[{timestamp}] ❌ [bold red]ERROR:[/bold red] Failed to save file → {e}")
