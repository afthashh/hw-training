import scrapy

class ExampleSpider(scrapy.Spider):
    name = 'spider_eg'
    start_urls = ['https://example.com']

    def parse(self, response):
        title = response.css('h1::text').get()
        yield {'title': title}
