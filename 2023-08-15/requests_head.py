# HEAD

import requests

response = requests.head('https://jsonplaceholder.typicode.com/posts/1')
print(response.headers)

