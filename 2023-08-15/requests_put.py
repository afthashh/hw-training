# PUT

import requests

url = "https://jsonplaceholder.typicode.com/posts/1"

data = {"userId": 1, "id": 1, "title": "Updated Title", "body": "Updated Body"}

response = requests.put(url, json=data)

print("Status Code:", response.status_code)
print("Response Content:")
print(response.text)
