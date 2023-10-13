import requests
import csv
from parsel import Selector
from urllib.parse import urljoin

class Bayut:
    def __init__(self):
        self.start_url = "https://www.bayut.eg/en/egypt/properties-for-sale/"
        self.visited_urls = set()
        self.counter = 0
        self.page = 2
        self.headers = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "en-US,en;q=0.9",
            "Cache-Control": "max-age=0",
            "Referer": "https://www.bayut.eg/",
            "Sec-Ch-Ua": "\"Google Chrome\";v=\"117\", \"Not;A=Brand\";v=\"8\", \"Chromium\";v=\"117\"",
            "Sec-Ch-Ua-Mobile": "?0",
            "Sec-Ch-Ua-Platform": "\"Windows\"",
            "Sec-Fetch-Dest": "document",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-Site": "same-origin",
            "Sec-Fetch-User": "?1",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"
        }
        self.csv_initialized = False

    def start(self):
        response = requests.get(self.start_url, headers=self.headers)
        print(response.status_code)
        if response.status_code == 200:
            selector = Selector(text=response.text)
            self.parse(selector)

    def parse(self, selector):
        apartments = selector.xpath('//article[contains(@class, "ca2f5674")]')
        for apartment in apartments:
            listing_url = apartment.xpath('.//div[contains(@class, "_4041eb80")]/a/@href').get()
            full_listing_url = urljoin("https://www.bayut.eg/", listing_url)
            
            if full_listing_url not in self.visited_urls:
                self.visited_urls.add(full_listing_url)
                response = requests.get(full_listing_url)
                if response.status_code == 200:
                    product_selector = Selector(text=response.text)
                    data = {
                        'property_url': full_listing_url,
                    'title': product_selector.xpath('//div[@aria-label="Property overview"]//h1[@class="fcca24e0 fontCompensation"]/text()').get(),
                    'reference_no': product_selector.xpath('//span[.="Reference no."]/following-sibling::span/text()').get(),
                    'purpose': product_selector.xpath("//span[@aria-label='Purpose']/text()").get(),
                    'type': product_selector.xpath("//span[@aria-label='Type']/text()").get(),
                    'added_on': product_selector.xpath("//span[@aria-label='Reactivated date']/text()").get(),
                    'furnishing': product_selector.xpath("//span[@class='_812aa185' and @aria-label='Furnishing']/text()").get(),
                    'currency': product_selector.xpath("//span[@aria-label='Currency']/text()").get(),
                    'amount': product_selector.xpath("//span[@aria-label='Price']/text()").get(),
                    'location': product_selector.xpath("//div[@aria-label='Property header']/text()").get(),
                    'bedrooms': product_selector.xpath('//span[@class="fc2d1086"]/text()').get(),
                    'bathrooms': product_selector.xpath("//span[@aria-label='Baths']/span/text()").get(),
                    'size': product_selector.xpath("//span[@aria-label='Area']/span/span/text()").get(),
                    'agent_name': product_selector.xpath("//span[@aria-label='Agent name']/text()").get(),
                    'img_url': product_selector.xpath("//div[@aria-label='Gallery Dialog']//div[@class='_22da360b']//div[@class='fe270b0a']//img/@src").getall(),
                    'breadcrumbs': product_selector.xpath("//div[@class='_74ac503e' and @aria-label='Breadcrumb']//span[@class='_327a3afc']/text()").getall(),
                    'description': product_selector.xpath("//div[@aria-label='Property description']/div/span/text()").getall()
                    }
                    if self.counter < 1000:
                        self.save_to_csv(data)
                        self.counter += 1
                        if self.counter >= 1000:
                            print("Reached the response limit")
                            return
        self.navigate_to_next_page()

    def navigate_to_next_page(self):
        next_page_url = f"https://www.bayut.eg/en/egypt/properties-for-sale/?page={self.page}"
        print("--------------------------------------------------------")
        print(next_page_url)
        # headers = {'User-Agent': self.user_agent}
        response = requests.get(next_page_url, headers=self.headers)
        self.page += 1

        if response.status_code == 200:
            selector = Selector(text=response.text)
            self.parse(selector)

    def save_to_csv(self, data):
        filename = "bayut_fulldata1.csv"
        with open(filename, "a", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=data.keys())
            if not self.csv_initialized:
                writer.writeheader()
                self.csv_initialized = True
            writer.writerow(data)

if __name__ == '__main__':
    scraper = Bayut()
    scraper.start()

