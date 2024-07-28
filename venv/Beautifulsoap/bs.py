from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://pythonscraping.com/pages/page1.html")
bsObj = BeautifulSoup(html.read(), "html.parser")
print(bsObj.h1)
# 아래 두 개는 같다.
# print(bsObj.html.body.h1)
# print(bsObj.html.h1)

