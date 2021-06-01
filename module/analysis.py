# -*- coding: utf-8 -*-

import json
import my_modules as mm

with open('./data/keywordsnofood.json', 'r', encoding='utf8') as lists:
    keywords = json.load(lists)
word_list = keywords


naver_dict = {}
with open('./data/naver_blog_cr.json', 'r', encoding='utf8') as f:
    naver_blog = json.load(f)

mm.sameword(naver_blog, word_list, naver_dict)
sort_naver_dict = sorted(naver_dict.items(),key=lambda x: x[1], reverse=True)
f_2 = open('./data/naver_keyword.json', 'w+', encoding='utf8')
f_2.write(json.dumps(sort_naver_dict, ensure_ascii=False))



jb_dict = {}
with open('./data/jpblog.json', 'r', encoding='utf8') as f_jb:
    jb_blog = json.load(f_jb)

mm.sameword(jb_blog, word_list, jb_dict)
sort_jb_dict = sorted(jb_dict.items(),key=lambda x: x[1], reverse=True)
f_2 = open('./data/jb_keyword.json', 'w+', encoding='utf8')
f_2.write(json.dumps(sort_jb_dict, ensure_ascii=False))

print(sort_jb_dict)




# mm.analys(naver_blog,naver_dict)
# sort_naver_dict = sorted(naver_dict.items(),key=lambda x: x[1], reverse=True)
# f_2 = open('./data/naver_keyword.json', 'w+', encoding='utf8')
# f_2.write(json.dumps(sort_naver_dict, ensure_ascii=False))