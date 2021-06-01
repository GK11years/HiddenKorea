# -*- coding: utf-8 -*-

import json
import my_modules as mm

naver_dict = {}

with open('./data/naver_blog_cr.json', 'r', encoding='utf8') as f:
    naver_blog = json.load(f)

word_list = ["서울", "남산","한옥마을","카페","한강","닭한마리","둔치공원"]

mm.sameword(naver_blog, word_list, naver_dict)
sort_naver_dict = sorted(naver_dict.items(),key=lambda x: x[1], reverse=True)
f_2 = open('./data/naver_keyword.json', 'w+', encoding='utf8')
f_2.write(json.dumps(sort_naver_dict, ensure_ascii=False))

print(sort_naver_dict)



# mm.analys(naver_blog,naver_dict)
# sort_naver_dict = sorted(naver_dict.items(),key=lambda x: x[1], reverse=True)
# f_2 = open('./data/naver_keyword.json', 'w+', encoding='utf8')
# f_2.write(json.dumps(sort_naver_dict, ensure_ascii=False))