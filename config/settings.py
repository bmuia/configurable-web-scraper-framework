SITE = [
    {
        "url": "https://books.toscrape.com/",
        "max_attempts": 3,
        "back_off": 2,
        "container_selector": "article.product_pod",
        "selectors": {
            "title": "h3 a",
            "price": "p.price_color"
        }
    },
]
