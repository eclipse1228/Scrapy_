from urllib.request import  urlopen
from bs4 import BeautifulSoup

html = urlopen("http://pythonscraping.com/pages/page3.html")
bs = BeautifulSoup(html, "html.parser")

for child in bs.find('table',{'id':'giftList'}).children:
    print(child)
# children은 자식 태그만 출력한다.

# 만약 , children 대신 descendants를 사용하면 자손 태그를 모두 출력한다.
# for child in bs.find('table',{'id':'giftList'}).descendants:
#     print(child)

