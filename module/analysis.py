# -*- coding: utf-8 -*-

import json
import my_modules as mm

naver_dict = {}

with open('./data/naver_blog_cr.json', 'r', encoding='utf8') as f:
    naver_blog = json.load(f)

mm.analys(naver_blog,naver_dict)

sort_naver_dict = sorted(naver_dict.items(),key=lambda x: x[1], reverse=True)
print(sort_naver_dict)