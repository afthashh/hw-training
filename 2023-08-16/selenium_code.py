from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

driver.get('https://www.google.com')

search_box = driver.find_element("name", "q")

search_box.send_keys('Hashwave')
search_box.send_keys(Keys.RETURN) 

time.sleep(5)  

search_results = driver.find_elements("css selector", "h3")
for result in search_results:
    print(result.text)

driver.quit()
