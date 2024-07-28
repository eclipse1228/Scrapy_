# Web scraping with BeautifulSoup (트리 단방향)

from urllib.request import  urlopen
from bs4 import BeautifulSoup

html = urlopen("http://pythonscraping.com/pages/warandpeace.html")
bs = BeautifulSoup(html, "html.parser")

# nameList = bs.findAll('span',{'class':'green'}) # (tag,attr,text,limit,keyword) 형식으로 검색한다.
# nameList = bs.findAll({'h1','h2','h3','h4','h5','h6'})
# nameList = bs.findAll(text='the prince') # 텍스트로 검색한다.
nameList = bs.findAll(id='text') # id로 검색한다. == bs.findAll('',{'id':'text'}) 의미가 같다. , 단 keyword 매개변수는 and처럼 동작한다.
for name in nameList:
    print(name.get_text()) # 태그 구조를 지우고 텍스트만 출력한다.
