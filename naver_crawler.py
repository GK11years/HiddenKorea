from bs4.element import ResultSet
import requests
from bs4 import BeautifulSoup

url_list =[]

def pop_url(loca):
    baseUrl = 'https://search.naver.com/search.naver?where=post&sm=tab_jum&query='

    url = baseUrl + loca
    response = requests.get(url)
    soup=BeautifulSoup(response.text,"html.parser")
    result = soup.find_all(class_='api_txt_lines total_tit')

    for i in result:
        url_list.append(i.attrs['href'])

def pop_text(url_list):
    for i in url_list:
        response = requests.get(i)

        soup = BeautifulSoup(response.content, "html.parser")
        iframe_src = soup.select_one("#mainFrame").attrs["src"]

        response = requests.get(f"https://blog.naver.com{iframe_src}")
        soup = BeautifulSoup(response.text, "html.parser")

        result_text = soup.select_one('.se-main-container')

        result_text = result_text.find_all('span')

        for i in result_text:
            print(i.text)


pop_url('여행지')
# print(url_list)
# print(len(url_list))
pop_text(url_list)


