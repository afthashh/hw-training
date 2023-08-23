# DELETE

import requests

url = "https://jsonplaceholder.typicode.com/posts/1"

response = requests.delete(url)

print("Status Code:", response.status_code)
