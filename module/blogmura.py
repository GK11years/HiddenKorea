import requests
from bs4 import BeautifulSoup


def remove_tags(results):  # remove tag
    soup = BeautifulSoup(results, "html.parser")

    for data in soup(['style', 'script']):
        # Remove tags
        data.decompose()
        # return data by retrieving the tag content
    return ' '.join(soup.stripped_strings)


# 1. 순위별로 크롤링
# 2. 블로그 1개당 하나의 텍스트파일로 저장
# 3. 텍스트파일을 읽어와서 번역 한 뒤 JSON 파일 형식으로 저장
request_headers = {
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36"}


###
page_number = 3
url_list = []
# word = "ソウル旅行, ソウル旅行地, ソウルの見どころ, ソウルの名所, ソウルの見どころ"
word = "ソウルの名所"
while True:

    URL = f"https://blogmura.com/search/posts?q={word}&p={page_number}"

    results = requests.get(URL, headers=request_headers)
    soup = BeautifulSoup(results.text, "html.parser")
    blog_links = soup.select("ul.blog-list div.blog-image a")
    for links in blog_links:
        link = links["href"]
        url_list.append(link)
        print(link)

    print(len(url_list))

    page_number += 1
    if page_number == 11:  # pagination
        break

###
blog_number = 1

for URL in url_list:
    results = requests.get(URL, headers=request_headers, verify=False)
    results.encoding = "UTF-8"
    test_ = remove_tags(results.text)
    print(len(test_))

<<<<<<< HEAD
    with open(f"../data/jpblog/{blog_number}.txt", "w") as file:
        text = file.write(test_)
=======
    with open(f"../data/jpblog/{blog_number}.txt", "w", encoding='utf8') as file:
       text = file.write(test_)
>>>>>>> 9490b3e7dd23569b303b7a835a034db448f3d1a1

    blog_number += 1
