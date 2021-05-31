from konlpy.tag import Mecab
from collections import Counter
import requests
from urllib.parse import quote
from os import close
from bs4.element import ResultSet
from bs4 import BeautifulSoup

# mecab 이용하여 명사만 추출, count 이용하여 중복 제거
def analys(cr_list, big_dict):
    mecab = Mecab()
    for i in cr_list:
        noun_list = mecab.nouns(i)
        count = Counter(noun_list)
        for j , k in count.most_common():
            key_ = j
            count_ = k
            if (len(key_) >= 2) :
                try:
                    big_dict[key_] += 1
                except KeyError:
                    big_dict[key_] = 1


client_id = "Y7yiVWADNUvhJBbOKnpc"
client_secret = "O59KsUaLyt"

# 네이버 api call
def call(keyword, start):
    encText = quote(keyword)
    url = "https://openapi.naver.com/v1/search/blog?query=" + encText + "&display=100" + "&start=" + str(start)
    result = requests.get(url=url, headers={"X-Naver-Client-Id":client_id,"X-Naver-Client-Secret":client_secret})
    print(result)  # Response [200]
    return result.json()
 
# 100개의 검색 결과 받아오기
def get100results(keyword):
    lists = []
    a = call(keyword, 1)['items']
    for i in range(len(a)):
        lists.append(str(a[i]['link']))
        # print(a[i]['link'])
    return lists

def pop_text(url_list):
    response = requests.get(url_list)
    soup = BeautifulSoup(response.content, "html.parser")
    iframe_src = soup.select_one("#mainFrame").attrs["src"]

    response = requests.get(f"https://blog.naver.com{iframe_src}")
    soup = BeautifulSoup(response.text, "html.parser")
    text_str = ""

    try:
        result_text = soup.select_one('.se-main-container')
        result_text = result_text.find_all('span') 
        
        for i in result_text:
            text_str += i.text.strip()
    
    except:
        None
    
    return text_str