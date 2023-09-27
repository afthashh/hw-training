import scrapy

class MySpider(scrapy.Spider):
    name = 'response_eg'
    
    def start_requests(self):
        yield scrapy.Request(url='https://example.com', callback=self.parse)
    
    def parse(self, response):  
        title = response.css('title::text').get()
        yield {'title': title}
