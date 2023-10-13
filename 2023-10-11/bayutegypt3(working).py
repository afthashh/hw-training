import requests
import csv
from parsel import Selector
from urllib.parse import urljoin  # Import the urljoin function

class Bayut:
    def __init__(self):
        self.start_url = "https://www.bayut.eg/en/egypt/properties-for-sale/"
        self.counter = 0
        self.page=2
        self.user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'
        self.csv_initialized = False

    def start(self):
        headers = {'User-Agent': self.user_agent}
        response = requests.get(self.start_url, headers=headers)
        print(response.status_code)
        # print(response.reason)
        if response.status_code == 200:
            selector = Selector(text=response.text)
            self.parse(selector)

    def parse(self, selector):
        apartments = selector.css('article.ca2f5674')
        # print(apartments)
        for apartment in apartments:
            listing_url =apartment.css('._4041eb80 a ::attr(href)').get()
            full_listing_url = urljoin("https://www.bayut.eg/", listing_url)
            response = requests.get(full_listing_url)
            # print(response)
            if response.status_code == 200:
                product_selector = Selector(text=response.text)
                self.parse_property(product_selector, full_listing_url)
        next_page_url = f"https://www.bayut.eg/en/egypt/properties-for-sale/?page={self.page}"
        print("--------------------------------------------------------")
        print(next_page_url)
        
        headers = {'User-Agent': self.user_agent}
        response = requests.get(next_page_url, headers=headers)
        self.page += 1
               
        if response.status_code == 200:
            selector = Selector(text=response.text)
            self.parse(selector)

        

    def parse_property(self, selector, property_url):
        data = {
            'property_url': property_url,
            'reference_no': selector.xpath('//span[.="Reference no."]/following-sibling::span/text()').get(),
            'purpose': selector.xpath("//span[@aria-label='Purpose']/text()").get(),
            'type': selector.xpath("//span[@aria-label='Type']/text()").get(),
            'added_on': selector.xpath("//span[@aria-label='Reactivated date']/text()").get(),
            'furnishing': selector.xpath("//span[@class='_812aa185' and @aria-label='Furnishing']/text()").get(),
            'price': {
                'currency': selector.xpath("//span[@aria-label='Currency']/text()").get(),
                'amount': selector.xpath("//span[@aria-label='Price']/text()").get(),
            },
            'location': selector.xpath("//div[@aria-label='Property header']/text()").get(),
            'bedrooms': selector.xpath('//span[@class="fc2d1086"]/text()').get(),
            'bathrooms': selector.xpath("//span[@aria-label='Baths']/span/text()").get(),
            'size': selector.xpath("//span[@aria-label='Area']/span/span/text()").get(),
            'agent_name': selector.xpath("//span[@aria-label='Agent name']/text()").get(),
            'img_url': selector.xpath("//div[@aria-label='Gallery Dialog']//div[@class='_22da360b']//div[@class='fe270b0a']//img/@src").getall(),
            'breadcrumbs': selector.xpath("//div[@class='_74ac503e' and @aria-label='Breadcrumb']//span[@class='_327a3afc']/text()").getall(),
            'description': selector.xpath("//div[@aria-label='Property description']/div/span/text()").getall(),
        }
        print(data)
        if self.counter < 1000:
            self.save_to_csv(data)
            self.counter +=1
            if self.counter >= 1000:
                print("reached thevresponse limit")

    def save_to_csv(self, data):
        filename = "bayut_fulldata1.csv"
        with open(filename, "a", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=data.keys())
            if not self.csv_initialized:
                writer.writeheader()  # Write the header only if it's the first time
                self.csv_initialized = True
            writer.writerow(data)

if __name__ == '__main__':
    scraper = Bayut()
    scraper.start()