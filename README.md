# Configurable Web Scraper Framework

A fully **YAML-driven, modular web scraping framework** in Python. This framework allows you to scrape multiple websites with configurable fields, supports dynamic output formats (JSON, CSV), and can be extended to databases or dashboards.

---

## Features

* **YAML Configuration** – Define multiple scrapers, fields, selectors, and output options easily.
* **Dynamic Field Parsing** – Extract multiple fields per site, including text and HTML attributes (`href`, `src`, `class`).
* **Multi-Site Support** – Run scrapers for multiple websites in a single pipeline.
* **Flexible Output** – Save results to JSON or CSV automatically.
* **Retry & Back-Off** – Handles temporary network errors.
* **CLI Integration** – Run scrapers using a single command (`belam run`).
* **Modular & Extensible** – Separate components for fetching, parsing, exporting, and pipeline management.

---

## Project Structure

```
configurable-web-scraper-framework/
│
├── config/
│   ├── config.yaml            # YAML configuration for all scrapers
│   └── config_utils.py        # Utility to load YAML configuration
│
├── scraper/
│   ├── framework.py           # WebScraper class
│   ├── fetcher.py             # fetch_url() function
│   ├── parser.py              # parse_scraper() function
│   ├── data_exporter.py       # save_file_results() function
│   ├── pipeline.py            # run_pipeline() function
│   └── cli.py                 # CLI entry point
│
├── setup.py                   # Package installation
├── requirements.txt           # Dependencies
├── LICENSE                     # MIT License
└── README.md
```

---

## Installation

1. Clone the repository:

```bash
git clone https://github.com/bmuia/configurable-web-scraper-framework.git
cd configurable-web-scraper-framework
```

2. Create a virtual environment:

```bash
python3 -m venv myenv
source myenv/bin/activate
```

3. Install the package:

```bash
pip install -e .
```

Dependencies (installed via `setup.py`):

* `requests>=2.31.0`
* `beautifulsoup4>=4.12.0`

---

## YAML Configuration

Example `config/config.yaml`:

```yaml
scrapers:
  - name: "Books To Scrape"
    base_url: "https://books.toscrape.com/"
    max_retries: 3
    back_off: 2
    item_container_selector: ".product_pod"
    fields:
      - name: title
        selector: "h3 a"
        attribute: "text"
      - name: price
        selector: ".price_color"
        attribute: "text"
      - name: rating
        selector: ".star-rating"
        attribute: "class"
    output:
      type: csv
      path: "results/books.csv"
```

* `fields` – List of dictionaries with `name`, `selector`.
* `output` – Defines type (`json` or `csv`) and save path.

---

## Usage

### Run via CLI

```bash
belam run
```

* Scrapes all sites in `config.yaml` and saves results according to output settings.

### Run via Python Script

```python
from scraper.pipeline import run_pipeline

results = run_pipeline()
print(results)
```

---

## Adding New Scrapers

1. Open `config/config.yaml`.
2. Add a new scraper under `scrapers:`:

```yaml
  - name: "New Site"
    base_url: "https://example.com/products"
    item_container_selector: ".product-item"
    fields:
      - name: product_name
        selector: ".title"
      - name: price
        selector: ".price"
    output:
      type: json
      path: "results/newsite.json"
```

3. Run `belam run` – no code changes needed.

---

## Extending the Framework

* **Pagination support** – Extend `WebScraper` or `pipeline.py` for multiple pages.
* **Database support** – Replace file-based saving with PostgreSQL, MongoDB, or SQLite.
* **Dashboard integration** – Connect the database to Grafana, Metabase, or Kibana.
* **Custom fetchers** – Add headers, cookies, or proxies in `fetch_url()`.

---

## Error Handling & Logging

* Missing selectors log a warning and skip that field.
* Network retries and back-off reduce temporary failures.
* Parser exceptions are caught and logged without stopping the pipeline.

---

## Contributing

1. Fork the repository.
2. Create a new branch: `git checkout -b feature/my-feature`.
3. Make your changes.
4. Test the framework.
5. Submit a pull request with a clear description.

---

## License

MIT License – free to use, modify, and distribute.
