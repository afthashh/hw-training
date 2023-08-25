import cloudscraper

scraper = cloudscraper.create_scraper()

print(scraper.get("http://quotes.toscrape.com").text)

# url = 'http://quotes.toscrape.com'

# response = scraper.get(url)

# if response.status_code == 200:
#     html_content = response.content.decode('utf-8')
#     print(html_content)
# else:
#     print(f"Request to {url} failed with status code {response.status_code}")


