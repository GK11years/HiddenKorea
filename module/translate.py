import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import emoji
import json


def remove_emoji(text):
    return emoji.get_emoji_regexp().sub(u'', text)


chromedriver = "./chromedriver"
options = webdriver.ChromeOptions()
options.add_argument("headless")
driver = webdriver.Chrome(chromedriver, options=options)

# 구글번역
driver.get("https://translate.google.com/?hl=ko&sl=ja&tl=ko&op=translate")

blog_contents_list = []
blog_number = 1
while True:
    test = driver.find_element_by_class_name("er8xn")
    with open(f"../data/jpblog/{blog_number}.txt", "r") as file:
        text = file.read()
        # print(remove_emoji(text))
        try:
            test.send_keys(remove_emoji(text))
        except:
            None
    # time.sleep(5)

    time.sleep(5)
    my_text = driver.find_elements_by_css_selector(".J0lOec")[0]
    translated_text = my_text.text

    blog_contents_list.append(translated_text)
    print(len(blog_contents_list))

    test.clear()

    blog_number += 1
    if blog_number == 42:
        break
# print(my_text.text)

# print(blog_contents_list)
with open("../data/jpblog2.json", "w", encoding="utf8") as json_file:
    st_json = json.dump(blog_contents_list, json_file, ensure_ascii=False)
