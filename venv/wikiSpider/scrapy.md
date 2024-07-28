# 1
- 실행은 scrapy runspider article.py

# 2 규칙에 의한 스파이더링

# 3 항목 만들기
수집한 모든 정보를 정리하는 Article 객체
items.py 파일에 정의 
- 새로운 Article 클래스를 만들려면 ArticleSpider 클래스도 그에 맞게 수정해야한다.
- scrapy runspider .\articleItems.py -articles.json -t json


# 4 파이프라이닝 
- process_items 메서드는 파이프라인 클래스에 필수 메서ㅡ이다. 이 메서드로 스파이더가 수집한 Items를 비동기적으로 전달한다.
- 이때 반환하는 파싱된 Article 객체는 로그에 기록 혹은 Json에 저장 됨
- 즉 parse_items 메서드(스파이더의) , process_items 메서드(파이프라인의) 두가지로 늘었음
- 