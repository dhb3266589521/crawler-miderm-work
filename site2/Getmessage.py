import requests
from bs4 import BeautifulSoup

movies=[]
#该函数目前用来爬取豆瓣新片榜
def get_title():
    url='https://movie.douban.com/chart'
    result=requests.get(url,timeout=10)
    soup=BeautifulSoup(result.text,'html.parser')

    getdata=soup.find_all('div',class_='pl2')
    for i in getdata:
        title=i.a.text.split('/')[0]
        actor=i.p.text
        movies.append({'title':title,'actor':actor})

    return movies