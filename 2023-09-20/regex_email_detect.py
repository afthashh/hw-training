import re

txt = "Sam~_-2023@yahoo.com"
x = re.findall("[\w~-]+@[\w.]+", txt)
print(x)
