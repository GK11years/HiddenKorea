from bs4 import BeautifulSoup
import requests

# Test URL
TESTURL = "https://search.yahoo.co.jp/search?p=%E9%9F%93%E5%9B%BD%E6%97%85%E8%A1%8C&fr=top_ga1_sa&ei=UTF-8&ts=23396&aq=-1&oq=&at=&ai=0789d535-5a13-4ae5-8df9-fbd30cbb8c99"
request_headers = {
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36"}


# Remove all html tag
# Reference
# https://stackoverflow.com/questions/30565404/remove-all-style-scripts-and-html-tags-from-an-html-page/30565420

def remove_tags(results):
    soup = BeautifulSoup(results, "html.parser")

    # for data in soup(['style', 'script']):
    # Remove tags
    #    data.decompose()
    # return data by retrieving the tag content
    return ' '.join(soup.stripped_strings)


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
    print(remove_tags(results))
