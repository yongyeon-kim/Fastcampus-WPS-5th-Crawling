import naverwebtooncrawler

class NaverWebtoon:
    def __init__(self, webtoon_id, weekday):
        self.webtoon_id = webtoon_id
        self.weekday = weekday
        self.episode_list = []

    def get_info(self):
        return '정보 리턴'

    def view_last_episode(self):
        return ''

    def view_episode_list(self, num=1):
        crawl_page = naverwebtooncrawler(self.webtoon_id, self.weekday)
        return_list = crawl_page.crawl_page(num)
        return return_list

    def save_webtoon(self, create_html=False):
        if create_html:
            return '다운받은 웹툰을 볼 수 있는 html까지 생성해서 저장'
        return '특정 경로에 웹툰 전체를 다운받아서 저장'


titleId = '662774'
weekday = 'wed'
page = '1'

naver_webtoon = NaverWebtoon(titleId, weekday)
naver_webtoon.view_episode_list(page)