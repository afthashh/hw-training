# URLLIB

# urllib.requests
# import urllib.request

# url = 'https://www.example.com'

# try:
#     response = urllib.request.urlopen(url)
#     data = response.read().decode('utf-8')
#     print(data)
# except urllib.error.HTTPError as e:
#     print(f"HTTP Error: {e.code} {e.reason}")
# except urllib.error.URLError as e:
#     print(f"URL Error: {e.reason}")




# urllib.parse
# from urllib.parse import urlparse, urljoin

# Parsing a URL
# url = 'https://www.example.com/path/page.html?query=param#fragment'
# parsed_url = urlparse(url)
# print(parsed_url)

# base_url = 'https://www.example.com/path/'
# relative_url = 'subpage.html'
# absolute_url = urljoin(base_url, relative_url)
# print(absolute_url)



# urllib.error
# import urllib.request
# import urllib.error

# url = 'https://www.nonexistent-website.com'

# try:
#     response = urllib.request.urlopen(url)
# except urllib.error.HTTPError as e:
#     print(f"HTTP Error: {e.code} {e.reason}")
# except urllib.error.URLError as e:
#     print(f"URL Error: {e.reason}")



# urllib.robotparser
from urllib.robotparser import RobotFileParser

robot_parser = RobotFileParser()
robot_parser.set_url('https://www.example.com/robots.txt')
robot_parser.read()

user_agent = 'MyBot'
can_crawl = robot_parser.can_fetch(user_agent, '/private-page/')
print(f"Can crawl '/private-page/': {can_crawl}")
