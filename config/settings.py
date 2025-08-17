
SITE = [
    {
        "url": "https://books.toscrape.com/",  # Should succeed
        "max_attempts": 3,
        "back_off": 2,
    },
    {
        "url": "https://httpbin.org/status/403",  # Forbidden (403)
        "max_attempts": 3,
        "back_off": 2,
    },
    {
        "url": "https://httpbin.org/status/404",  # Not found (404)
        "max_attempts": 3,
        "back_off": 2,
    },
    {
        "url": "https://httpbin.org/delay/5",  # Delayed response (tests timeout)
        "max_attempts": 3,
        "back_off": 2,
    }
]
