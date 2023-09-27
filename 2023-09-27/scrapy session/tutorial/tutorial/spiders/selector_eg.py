import scrapy

class MySpider(scrapy.Spider):
    name = 'selector_eg'
    
    def start_requests(self):
        yield scrapy.Request(url='https://example.com', callback=self.parse)
    
    def parse(self, response):
        title = response.css('title::text').get()
        
        heading = response.xpath('//h1/text()').get()
        
        data = {
            'title': title,
            'heading': heading,
        }
        
        yield data
