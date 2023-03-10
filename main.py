import requests, lxml
from bs4 import BeautifulSoup as bs

url="https://www.rbc.ru/economics/"

headers= {
    "user-agent":"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Mobile Safari/537.36",
    "X-Requested-Width":"XMLHttpRequest"
}

resp = requests.get(url,headers=headers)

soup = bs(resp.text, "lxml")
#cat=soup.class('category')

news= soup.find_all(class_= "item__wrap")

for n in news:
    data=n.find(class_='item__category').text.strip()
    name = n.find(class_='item__title').text.strip()
    print(data,name)







