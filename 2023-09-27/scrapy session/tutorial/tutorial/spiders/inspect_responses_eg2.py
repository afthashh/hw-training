import scrapy
from scrapy.shell import inspect_response

class MySpider(scrapy.Spider):
    name = 'myspider'
    start_urls = ['http://quotes.toscrape.com']

    def parse(self, response):
        # Inspect the response interactively
        inspect_response(response, self)

