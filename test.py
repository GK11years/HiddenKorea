import pandas as pd
from pandas import DataFrame
# isted_comp_df = pd.read_html(
#     'http://kind.krx.co.kr/corpgeneral/corpList.do?method=download&searchType=13', header=0)[0]

# print(isted_comp_df)
# df = DataFrame(isted_comp_df, columns=['종목코드'])

# print(df)


# target = 2404

# a = format(target, '06')
# print(a)
import requests
import pandas as pd
from pandas import DataFrame
headers = {'User-agent':
           "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"}
df = pd.DataFrame()


j_code_list = ["163560", "004890", "030790"]

for j_code in j_code_list:

    try:
        for i in range(1, 101):
            url = f'https://finance.naver.com/item/sise_day.nhn?code={j_code}&page=' + str(
                i)
            table = pd.read_html(requests.get(
                url, headers=headers).text, encoding="cp949")
            df_temp = table[0]
            df = df.append(df_temp, ignore_index=True)
        Hyundai_Car_stock = df.dropna()
        #Hyundai_Car_stock.to_csv('Hyundai_car_stock.csv', encoding='cp949')
    except:
        None

print(Hyundai_Car_stock.head(200))


headers = {'User-agent':
           "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"}
df = pd.DataFrame()


j_code_list = ["163560", "004890", "030790"]

for j_code in j_code_list:

    try:
        for i in range(1, 101):
            url = f'https://finance.naver.com/item/sise_day.nhn?code={j_code}&page=' + str(
                i)
            table = pd.read_html(requests.get(
                url, headers=headers).text, encoding="cp949")
            df_temp = table[0]
            df = df.append(df_temp, ignore_index=True)
        Hyundai_Car_stock = df.dropna()
        #Hyundai_Car_stock.to_csv('Hyundai_car_stock.csv', encoding='cp949')
    except:
        None

print(Hyundai_Car_stock.head(200))


def make_csv(x):
    import requests as rq
    import pandas as pd
    from pandas import DataFrame
    headers = {'User-agent':
               "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"}
    df = pd.DataFrame()
    for i in range(1, 3):
        url = 'https://finance.naver.com/item/sise_day.nhn?code={0}&page='.format(
            x) + str(i)
        table = pd.read_html(
            rq.get(url, headers=headers).text, encoding="cp949")
        df_temp = table[0]
        df = df.append(df_temp, ignore_index=True)
    stock = df.dropna()
    #stock.to_csv('{0}_stock.csv'.format(x), encoding = 'cp949')
    print(stock)


for i in range(x):
    #b = x[i]
    make_csv("{}".format(b))
make_csv
