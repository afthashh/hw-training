import scrapy

class MySpider(scrapy.Spider):
    name = 'formrequest_eg'
    
    def start_requests(self):
        yield scrapy.FormRequest(url='https://quotes.toscrape.com/login',
                                  formdata={'username': 'username', 'password': 'password'},
                                  callback=self.parse_login)
    
    def parse_login(self, response):
        pass
