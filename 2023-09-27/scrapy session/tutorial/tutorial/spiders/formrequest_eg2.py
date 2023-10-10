import scrapy

class MySpider(scrapy.Spider):
    name = 'formrequest_eg2'
    
    def start_requests(self):
        yield scrapy.FormRequest(url='https://quotes.toscrape.com/login',
                                  formdata={'username': 'username', 'password': 'password'},
                                  callback=self.parse_login)
    
    def parse_login(self, response):

        for quote in response.css('div.quote'):
                        quote_text = quote.css('span.text::text').get()
                        author = quote.css('span small.author::text').get()
                        tags = quote.css('div.tags a.tag::text').getall()
                        
                        yield {
                            'quote': quote_text,
                            'author': author,
                            'tags': tags
                        }