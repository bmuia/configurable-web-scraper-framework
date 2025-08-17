# tests/test_fetcher.py
import pytest
from scraper.fetcher import fetch_url

def test_fetch_success():
    
    url = "https://books.toscrape.com/"
    response = fetch_url(url)
    assert response is not None
    assert response.status_code == 200

def test_fetch_fail():
  
    url = "https://httpbin.org/status/403"
    response = fetch_url(url, max_attempts=2, back_off=0)
    assert response is None
