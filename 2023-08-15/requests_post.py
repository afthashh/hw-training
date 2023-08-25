# POST

import requests

url = "https://httpbin.org/post"

data = {"Name": "John", "Age": "30"}

response = requests.post(url, data=data)

print("Status Code:", response.status_code)
print("Response Content:")
print(response.text)
