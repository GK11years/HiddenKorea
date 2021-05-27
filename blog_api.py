import requests
from urllib.parse import quote
import json


client_id = "Y7yiVWADNUvhJBbOKnpc"
client_secret = "O59KsUaLyt"

# 네이버 api call
def call(keyword, start):
    encText = quote(keyword)
    url = "https://openapi.naver.com/v1/search/blog?query=" + encText + "&display=100" + "&start=" + str(start)
    result = requests.get(url=url, headers={"X-Naver-Client-Id":client_id,"X-Naver-Client-Secret":client_secret})
    print(result)  # Response [200]
    return result.json()
 
# 1000개의 검색 결과 받아오기
def get1000results(keyword):
    lists = []
    for num in range(0,10):
        # list = list + call(keyword, num * 100 + 1)['items']
        a = call(keyword, num * 100 + 1)['items']
        for i in range(len(a)):
            lists.append(str(a[i]['link']))
            # print(a[i]['link'])
    return lists


list_1000_url = []
sur_list = ["서울여행", '서울명소','서울가볼만한곳']

for i in sur_list:
    result = get1000results(i)
    list_1000_url.append(result)

file = open('./tour.json', 'w+')
file.write(json.dumps(list_1000_url))
