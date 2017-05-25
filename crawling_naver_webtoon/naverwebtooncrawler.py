import re
import requests
from bs4 import BeautifulSoup


class NaverWebtoonCrawler:
    _naver_webtoon_url = 'http://comic.naver.com/webtoon/list.nhn?'
    _naver_webtoon_dedtail = 'http://comic.naver.com/webtoon/detail.nhn?'

    def __init__(self, webtoon_id, weekday):
        self.webtoon_id = webtoon_id
        self.weekday = weekday

    def crawl_page(self, page_num):
        return_list = self.get_html(self._naver_webtoon_url, page_num)
        return return_list

    def crawl_episode(self, episode_num=None):

        # episode_num의 값이 없으면 마지막 에피소드 출력
        if not episode_num:
            # 마지막 에피소드 출력
            return_list = self.get_html(self._naver_webtoon_url, 1)
            return return_list[0]

        # 값이 무언가가 있을 경우 전체 에피소드를 조회
        all_episodes_list = []
        for i in range(1, 58):
            all_episodes_list += self.get_html(self._naver_webtoon_url, i)

        # all일 경우 모두 출력
        if episode_num == 'all':
            return all_episodes_list
        # 특정 숫자가 있을 경우 해당 에피소드 출력
        else:
            return all_episodes_list[(-episode_num)]


    def get_html(self, url, page_num):
        url_params = {
            'titleId': self.webtoon_id,
            'weekday': self.weekday,
            'page': page_num
        }
        response = requests.get(url, url_params)
        soup = BeautifulSoup(response.text, 'lxml')

        table = soup.find('table', class_='viewList')
        tr_list = table.find_all('tr')

        return_list = []
        for tr in tr_list:
            if not tr.find('td', class_='title'):
                continue

            episode_title = tr.find('td', class_='title').find('a').text
            return_list.append(episode_title)

        return return_list

    def get_episode_img(self, episode_num):
        params = {
            'titleId': self.webtoon_id,
            'weekday': self.weekday,
            'no': episode_num
        }
        response = requests.get(self._naver_webtoon_dedtail,params)
        soup = BeautifulSoup(response.text, 'lxml')

        div = soup.find('div', class_='wt_viewer')
        img_list = div.find_all('img')

        test_list = [img['src'] for img in img_list]

        return test_list



    def get_episode_num_list(self, url, page_num):
        url_params = {
            'titleId': self.webtoon_id,
            'weekday': self.weekday,
            'page': page_num
        }
        response = requests.get(url, url_params)

        pattern = r'(?<=&no=)\d*(?=&)'

        m_list = re.finditer(pattern, response.text)
        episode_num_list = list(set([m.group() for m in m_list]))
        episode_num_list.sort(reverse=True)
        return episode_num_list



##################################################


class NaverWebtoon:
    def __init__(self, webtoon_id, weekday):
        self.webtoon_id = webtoon_id
        self.weekday = weekday
        self.episode_list = []
        self.crawl_page = NaverWebtoonCrawler(self.webtoon_id, self.weekday)

    def get_info(self):
        return '정보 리턴'

    # - 특정 페이지 에피소드 리스트 출력
    def view_episode_list(self, num=1):
        return_list = self.crawl_page.crawl_page(num)
        return return_list

    # - 마지막 에피소드 출력
    def view_last_episode(self):
        return_list = self.crawl_page.crawl_episode()
        return return_list

    # - 에피소드 전체 출력
    def view_episode_all(self):
        return_list = self.crawl_page.crawl_episode('all')
        return return_list

    # - 특정 에피소드 출력
    def view_episode(self, episode_num):
        return_list = self.crawl_page.crawl_episode(episode_num)
        return return_list

    # - 특정 에피소드 이미지 리스트 출력
    def view_episode_img_list(self, episode_num):
        return_list = self.crawl_page.get_episode_img(episode_num)
        return return_list


    def download_episode(self):
        pass



    def save_webtoon(self, create_html=False):
        if create_html:
            return '다운받은 웹툰을 볼 수 있는 html까지 생성해서 저장'
        return '특정 경로에 웹툰 전체를 다운받아서 저장'


titleId = '21815'
weekday = 'mon'
page = '1'

naver_webtoon = NaverWebtoon(titleId, weekday)

# 1. 전체 에피소드 리스트를 가져오기
#episode_list_all = naver_webtoon.view_episode_all()
#print(episode_list_all)

# - 마지막 에피소드
#episode_last = naver_webtoon.view_last_episode()
#print(episode_last)

# - 특정 에피소드
#episode_view = naver_webtoon.view_episode(3)
#print(episode_view)

# - 특정 페이지 에피소드 리스트 출력
#episode_list = naver_webtoon.view_episode_list(page)
#print(episode_list)

##################################################################

# 2. 에피소드 번호를 입력하면(no) 내부의 웹툰 이미지 주소를 가져오기 (여러장의 이미지로 분할되어있음)
#episode_img_list = naver_webtoon.view_episode_img_list(564)
#print(episode_img_list)



##################################################################

# 3. 썸네일이미지 또는 내부 웹툰 이미지를 저장



##################################################################

# 4. 모든것을 통합해서 실행하면 웹툰을 각 화별 폴더를 생성해서 저장하기


##################################################################

# 5. 저장한 파일을 접근할 수 있는 HTML생성


