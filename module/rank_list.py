import json


def chart():
    with open('./data/jb_keyword.json', 'r', encoding='utf8') as f_jb:
        jb_blog = json.load(f_jb)

    with open('./data/naver_keyword.json', 'r', encoding='utf8') as f_kb:
        kb_blog = json.load(f_kb)

    sub_list = []
    for i in jb_blog:
        for j in kb_blog:
            if j[0] in i[0]:
                sub_list.append(i[0])

    hidden_blog = []
    for i in kb_blog:
        hidden_blog.append(i[0])

    hidden_list = hidden_blog
    for i in sub_list:
        if i in hidden_list:
            hidden_list.remove(i)

    jb_list = []
    for i in jb_blog:
        jb_list.append(i[0])

    kb_list = []
    for i in kb_blog:
        kb_list.append(i[0])

    kb = kb_list[:10]
    jb = jb_list[:10]
    hd = hidden_list[:10]
    chart_list = {"korea": kb, "japan": jb, "hidden": hd}

    return(chart_list)


print(chart())
