# 네이버 검색 API예제는 블로그를 비롯 전문자료까지 호출방법이 동일하므로 blog검색만 대표로 예제를 올렸습니다.
# 네이버 검색 Open API 예제 - 블로그 검색
import os
import sys
import urllib.request
import json


client_id = "Y7yiVWADNUvhJBbOKnpc"
client_secret = "O59KsUaLyt"
encText = urllib.parse.quote("여행지")
url = "https://openapi.naver.com/v1/search/blog?query=" + encText # json 결과
# url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # xml 결과
# url = "https://blog.naver.com/hnmh2332?Redirect=Log&logNo=222304147863"
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request)
rescode = response.getcode()
if(rescode==200):
    response_body = response.read()
    # print(response_body.decode('utf-8'))
    result = json.loads(response_body.decode('utf-8'))
    for i in result['items']:
        print(i['title'], i['description'])
    # answer = result['items'][2]['title']
    # print(answer)
else:
    print("Error Code:" + rescode)
  

