# OPTIONS

import requests

response = requests.options('https://httpbin.org')
print(response.headers)
