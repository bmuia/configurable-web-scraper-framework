import os
import json
import csv
from datetime import datetime

def save_file_results(data, output_config):
    """
    Save scraped data to a file based on output configuration.

    :param data: List of dictionaries containing scraped items
    :param output: Dict with 'type' (json/csv) and optional 'path'
    """
    output_type = output_config.get("type", "json").lower()
    path = output_config.get("path", "data/output.json")
    os.makedirs(os.path.dirname(path), exist_ok=True)
    

    try:
        if output_type == "json":
            with open(path, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=4)

        elif output_type == "csv":
            if len(data) == 0:
                print(f"[INFO] No data to save for CSV at {path}")
                return

            keys = data[0].keys()
            with open(path, 'w', newline='', encoding='utf-8') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=keys)
                writer.writeheader()
                writer.writerows(data)

        else:
            print(f"[WARN] {datetime.now()} - Unsupported output type: {output_type}")

        print(f"[INFO] Data saved successfully to {path}")

    except Exception as e:
        print(f"[ERROR] {datetime.now()} - Failed to save file: {e}")
