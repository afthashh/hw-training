import scrapy

class MySpider(scrapy.Spider):
    name = 'requests_eg'
    
    def start_requests(self):
        urls = ['https://example.com/page1', 'https://example.com/page2']
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
    
    def parse(self, response):   
        pass
