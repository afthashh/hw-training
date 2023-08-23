# PATCH

import requests

url = "https://jsonplaceholder.typicode.com/posts/1"

data = {"title": "Updated Title"}

response = requests.patch(url, json=data)

print("Status Code:", response.status_code)
print("Response Content:")
print(response.text)
