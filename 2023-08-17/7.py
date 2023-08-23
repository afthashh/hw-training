import cloudscraper
url="https://example.com/"
scraper=cloudscraper.create_scraper()
response=scraper.get(url)
content=response.content
print(content)