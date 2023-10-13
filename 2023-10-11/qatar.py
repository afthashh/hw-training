import requests
from parsel import Selector
# import csv
class Qatarscraper:
    def __init__(self):
        self.start_url = "https://www.qatarliving.com/properties"
        self.counter = 0
        self.user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
    def start(self):
        headers = {'User-Agent':self.user_agent}
        response = requests.get(self.start_url,headers=headers)
        print(response.status_code)
        # print(response.reason)
        if response.status_code == 200:
            selector = Selector(text=response.text)
            self.parse(selector)
    def parse(self,selector):
        product_url = selector.xpath('//*[@class="vehicle-row"]//a[@class="vehicle-row-data"]/@href').getall()
        print(product_url)
5:25
if __name__ == "__main__":
    scraper = Qatarscraper()
    scraper.start()