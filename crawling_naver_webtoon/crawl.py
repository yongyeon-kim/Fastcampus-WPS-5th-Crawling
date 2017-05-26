# naver 패키지 내부의 NaverWebtoonCrawler클래스형 인스턴스를 생성 인스턴스에서 crawl_episode실행
from naver import NaverWebtoonCrawler

webtoon_id = '21815'

crawler = NaverWebtoonCrawler(webtoon_id)
crawler.crawl_episode(2)