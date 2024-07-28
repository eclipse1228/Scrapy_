from urllib.request import urlopen
from urllib.error import HTTPError, URLError

try:
    html = urlopen("http://pythonscraping.com/pages/page1.html")
except HTTPError as e:
    print(e)
    # return null, break, or do some other "Plan B"
except URLError as e:
    print("The server could not be found!")
else:
    # 프로그램을 계속 실행해야 하는 경우
    # 에러가 발생하지 않았을 때만 실행
    print(html.read())
