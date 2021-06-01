import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import json

chromedriver = "./chromedriver"
options = webdriver.ChromeOptions()
# options.add_argument("headless")
driver = webdriver.Chrome(chromedriver, options=options)

# 여행지 목록
driver.get("https://api.visitkorea.or.kr/search/commonList.do")
driver.find_element_by_xpath("//input[@title='전체']").click()
time.sleep(0.5)
driver.find_element_by_xpath("//input[@title='관광지']").click()
time.sleep(0.5)
driver.find_element_by_xpath("//input[@title='문화시설']").click()
time.sleep(0.5)
# driver.find_element_by_xpath("//input[@title='음식점']").click()
# time.sleep(0.5)
select = Select(driver.find_element_by_xpath("//select[@title='지역선택']"))
time.sleep(0.5)
select.select_by_visible_text('서울')
time.sleep(0.5)
select = Select(driver.find_element_by_xpath("//*[@id='numOfPage']"))
time.sleep(0.5)
select.select_by_visible_text('50개씩 보기')
time.sleep(0.5)
driver.find_element_by_xpath("//input[@id='search']").click()

# driver.find_element_by_xpath("//*[@id='content']/div[6]/a[3]").click()

#test = driver.find_element_by_class_name("er8xn")
num = 1
my_list = []
try:
    while True:
        for i in range(num, num+9):
            for number in range(1, 51):

                comment = driver.find_element_by_xpath(
                    f"//*[@id='listForm']/ul/li[{number}]/a/dl/dt").text
                print(comment)
                my_list.append(comment)
            driver.find_element_by_xpath(
                f"//*[@id='content']/div[6]/span/a[{i}]").click()
            time.sleep(0.3)
            print(len(my_list))
            ##pagination +=1
            # if pagination == 11:
        # time.sleep(0.5)
        driver.find_element_by_xpath("//*[@id='content']/div[6]/a[3]").click()
        time.sleep(1)
except:
    with open("../data/keywordsnofood.json", "w", encoding="utf8") as json_file:
        st_json = json.dump(my_list, json_file, ensure_ascii=False)
