from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

chromedriver = "./chromedriver"

options = webdriver.ChromeOptions()

driver = webdriver.Chrome(chromedriver, options=options)

# 구글번역
driver.get("https://www.google.com/search?q=%EA%B5%AC%EA%B8%80%EB%B2%88%EC%97%AD&oq=%EA%B5%AC%EA%B8%80%EB%B2%88%EC%97%AD&aqs=chrome.0.69i59l2j69i61l3.4482j0j9&sourceid=chrome&ie=UTF-8")
test = driver.find_element_by_id("tw-source-text-ta")
test.send_keys("Hello")

time.sleep(1)
my_text = driver.find_elements_by_css_selector("#tw-target-text")[0]
print(my_text.text)
