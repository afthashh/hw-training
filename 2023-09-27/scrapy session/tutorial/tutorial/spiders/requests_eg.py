import scrapy

class MySpider(scrapy.Spider):
    name = 'requests_eg'
    start_urls = ['http://quotes.toscrape.com/page/1/', 'http://quotes.toscrape.com/page/1']

    # def start_requests(self):
    #     urls = ['http://quotes.toscrape.com/page/1/', 'http://quotes.toscrape.com/page/1']
    #     for url in urls:
    #         yield scrapy.Request(url=url, callback=self.parse, dont_filter= True)
    
    def parse(self, response):   
        for quote in response.css('div.quote'):
            yield {
                'text': quote.css('span.text::text').get(),
                'author': quote.css('span small.author::text').get(),
                'tags': quote.css('div.tags a.tag::text').getall(),
            }
