from bs4 import BeautifulSoup

def parse_scraper(response, container_selector, selectors): 
    try:
        soup = BeautifulSoup(response.content, 'html.parser')
        results = []
        
        containers = soup.select(container_selector)

        for container in containers:
            item = {}
            for name, css in selectors.items():
                element = container.select_one(css)
                if element:
                    item[name] = element.get_text(strip=True)

            if item: 
                results.append(item)

        return results
    
    except Exception as e:
        print(f"[ERROR] {e}")
        return []
