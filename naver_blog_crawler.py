from bs4.element import ResultSet
import requests
from bs4 import BeautifulSoup
import json

def pop_text(url_list):
    response = requests.get(url_list)

    soup = BeautifulSoup(response.content, "html.parser")
    iframe_src = soup.select_one("#mainFrame").attrs["src"]

    response = requests.get(f"https://blog.naver.com{iframe_src}")
    soup = BeautifulSoup(response.text, "html.parser")

    result_text = soup.select_one('.se-main-container')

    result_text = result_text.find_all('span')

    for i in result_text:
        print(i.text)

with open('./tour.json', 'r') as f:
    url_list = json.load(f)

# print(len(url_list))
# print(url_list)
for i in range(len(url_list)):
    for j in url_list[i]:
        if 'blog.naver.com' in j:
            # print(j)
            pop_text(j)


