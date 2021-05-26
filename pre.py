from bs4.element import ResultSet
import requests
from bs4 import BeautifulSoup


response = requests.get('https://blog.naver.com/hnmh2332/222304147863')

soup = BeautifulSoup(response.content, "html.parser")
iframe_src = soup.select_one("#mainFrame").attrs["src"]

response = requests.get(f"https://blog.naver.com{iframe_src}")
soup = BeautifulSoup(response.text, "html.parser")

result_text = soup.select_one('.se-main-container')

result_text = result_text.find_all('span')

f = open('test.txt','w', encoding="UTF8")

for i in result_text:
    f.write(i.text)

f.close()
