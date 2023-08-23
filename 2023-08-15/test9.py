import requests

image_url = "https://upload.wikimedia.org/wikipedia/commons/5/55/Large_breaking_wave.jpg"

response = requests.get(image_url)

if response.status_code == 200:
    image_content = response.content

    with open("downloaded_image.jpg", "wb") as f:
        f.write(image_content)
        print("Image downloaded successfully.")
else:
    print("Failed to download image. Status code:", response.status_code)
