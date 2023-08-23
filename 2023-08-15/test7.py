# Parsel

import requests
from parsel import Selector

url = "https://www.python.org/"

response = requests.get(url)

selector = Selector(text=response.text)

title = selector.css("title::text").get()

print("Title:", title)
