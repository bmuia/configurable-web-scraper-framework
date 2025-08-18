import os
import json
import csv


def save_as_json(results, filename="output/results.json"):
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=4, ensure_ascii=False)


def save_as_csv(results, filename="output/results.csv"):
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    if not results:
        print("[WARN] No results to save.")
        return

    with open(filename, "w", newline="", encoding="utf-8") as f:
        fieldnames = results[0].keys()
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(results)
