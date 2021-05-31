import json
import my_modules as mm

list_100_url = []
sur_list = ["서울 가볼만한곳"]

for i in sur_list:
    result = mm.get100results(i)
    list_100_url.append(result)

f_2 = open('./data/naver_blog_cr.json', 'w+', encoding='utf8')

cr_list = []
for i in range(len(list_100_url)):
    for j in list_100_url[i]:
        if 'blog.naver.com' in j:
            cr_list.append(mm.pop_text(j))
f_2.write(json.dumps(cr_list, ensure_ascii=False))
