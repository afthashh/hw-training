import requests
from lxml import html

# URL of the properties website you want to scrape
url = 'https://www.bayut.eg/en/property/details-199068439.html'

# Send a GET request to the website
response = requests.get(url)

# Parse the HTML content of the page using lxml
tree = html.fromstring(response.content)

# Use XPath to extract data
# Replace 'your_xpath_expression' with your actual XPath expression
# For example, to extract property titles: titles = tree.xpath('your_xpath_expression_for_titles')
data = tree.xpath("//span[@aria-label='Reference']/text()")

# Print the extracted data to check the response
print(data)
