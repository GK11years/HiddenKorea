from bs4 import BeautifulSoup
import requests
import time

# Test URL
word = "韓国旅行"
page_number = str(10)
#TESTURL = f"https://search.yahoo.co.jp/search?p={word}&fr=top_ga1_sa&ei=UTF-8&ts=23396&aq=-1&oq=&at=&ai=0789d535-5a13-4ae5-8df9-fbd30cbb8c99"

TESTURL = f"https://search.yahoo.co.jp/search?p={word}&fr=top_ga1_sa&ei=UTF-8&ts=23396&aq=-1&ai=0789d535-5a13-4ae5-8df9-fbd30cbb8c99&b={page_number}1"

request_headers = {
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36"}


# Remove all html tag
# Reference
# https://stackoverflow.com/questions/30565404/remove-all-style-scripts-and-html-tags-from-an-html-page/30565420

def remove_tags(results):
    soup = BeautifulSoup(results, "html.parser")

    for data in soup(['style', 'script']):
        # Remove tags
        data.decompose()
        # return data by retrieving the tag content
    return ' '.join(soup.stripped_strings)


def yahoo_crawler():
    yahoo_list = []
    result = requests.get(TESTURL, headers=request_headers)
    soup = BeautifulSoup(result.text, "html.parser")
    # contents box of Main page
    contents = soup.select(".Contents__innerGroupBody .sw-CardBase")

    for content in contents:
        # url of inside content
        sub_url = content.select_one("a")["href"]

        results = requests.get(sub_url, headers=request_headers)
        results.encoding = "UTF-8"  # ISO-8859-1 to UTF-8
        results = results.text
        # print(results)
        remove_tage_results = remove_tags(results)
        print(remove_tage_results)
        # yahoo_list.append(temp)

    return results


yahoo_crawler()


def translater(text):

    translate_url = f"https://translate.google.com/?hl=ko&sl=ja&tl=ko&text={text}&op=translate"
    result = requests.get(translate_url, headers=request_headers)
    time.sleep(10)
    soup = BeautifulSoup(result.text, "html.parser")
    #translate_result = soup.select_one("div.J0lOec")
    # print(suop)


# translater("内の人気マッコリ居酒屋")


# print(yahoo_crawler())


# 제이슨파일이 필요해
# 리스트 양식
# 한글로된 한페이지가 1번에
# 두번쨰 페이지는 2번리스트
