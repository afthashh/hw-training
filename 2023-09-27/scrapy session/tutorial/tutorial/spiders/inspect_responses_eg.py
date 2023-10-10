import scrapy
from scrapy.shell import inspect_response

class MySpider(scrapy.Spider):
    name = "inspect_responses_eg"
    start_urls = [
        "http://example.com",
        "http://example.org",
        "http://example.net",
    ]

    def parse(self, response):
        # We want to inspect one specific response.
        if ".com" in response.url:       
            inspect_response(response, self)

        # Rest of parsing code.


# response.url
# response.css('h1::text').get()