import requests, lxml
from bs4 import BeautifulSoup as bs
from datetime import date, datetime
import sqlite3

def bd(a):
    conn = sqlite3.connect('news.sqlite')
    cur = conn.cursor()
    i=0
    for n in a:
        cur.execute("INSERT INTO news VALUES(?, ?, ?);", [i,n])
        conn.commit()
        i+=1

    conn.close()

def dt(date_):
    dt=''
    if ',' in date_:
        #dt=d.split(',')
        dt=date_
        if 'мар' in date_:
            dt='2023-03-'+date_.split(' ')[0]+date_.split(',')[1]
    else:
        dt=str(date.today())+' '+date_
    return dt

def main():
    url="https://www.rbc.ru/economics/"

    headers= {
        "user-agent":"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Mobile Safari/537.36",
        "X-Requested-Width":"XMLHttpRequest"
    }

    resp = requests.get(url,headers=headers)

    soup = bs(resp.text, "lxml")
    #cat=soup.class('category')

    news= soup.find_all(class_= "item__wrap")

    print('--[date]---[time]-----------------------[news headline]--------------------------')

    a=[]
    for n in news:
        date = dt(n.find(class_='item__category').text.strip())
        name = n.find(class_='item__title').text.strip()
        print(date,name)
        a.append([date,name])

    bd(a)

if __name__ == "__main__":
    main()




