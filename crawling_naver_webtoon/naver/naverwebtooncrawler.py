import os

import requests
import re
from bs4 import BeautifulSoup


class NaverWebtoonCrawler:
    _url_detail_base = 'http://comic.naver.com/webtoon/detail.nhn?' \
                       'titleId={webtoon_id}&' \
                       'no={episode_num}&' \
                       'weekday=wed'
    _url_list_base = 'http://comic.naver.com/webtoon/list.nhn?'

    def __init__(self):
        self.webtoon_id = 0

    def crawl_page(self, page_num):
        params = {
            'titleId': self.webtoon_id,
            'page': page_num
        }
        pattern_no = r'(?<=no=)\d*'
        response = requests.get(self._url_list_base, params)
        soup = BeautifulSoup(response.text, 'lxml')
        table = soup.find('table', class_='viewList')
        td_title = table.select('td.title')
        episode_title_list = [title.text.strip() for title in td_title]
        for title in episode_title_list:
            print(title)

    def crawl_episode(self, episode_num):
        self.make_content(episode_num)

    def crawl_last_episode(self):
        episode_num = self.select_last_episode_num(self._url_list_base, self.webtoon_id)
        self.make_content(episode_num)

    def crawl_all_episodes(self):
        episode_num = self.select_last_episode_num(self._url_list_base, self.webtoon_id)

        for i in range(1, episode_num+1):
            self.make_content(episode_num)

    def select_last_episode_num(self, url, webtoonId):
        print(url,webtoonId)
        params = {
            'titleId': webtoonId,
            'page': '1'
        }
        response = requests.get(self._url_list_base, params)
        soup = BeautifulSoup(response.text, 'lxml')
        episode_last_tag = soup.select_one('td.title > a')
        episode_num_pattern = r'(?<=no=)\d*'
        print(episode_last_tag)
        m = re.search(episode_num_pattern, str(episode_last_tag))
        print(m)
        episode_last_num = m.group()
        print(episode_last_num)
        return episode_last_num

    def make_content(self, episode_num):

        url_detail = self._url_detail_base.format(
            webtoon_id=self.webtoon_id,
            episode_num=episode_num
        )

        dir_path = './webtoon/{}/{}'.format(self.webtoon_id, episode_num)

        def make_episode_dir():
            # 이미지를 저장하기 위한 폴더 생성
            # exists로 이미 생성하려는 폴더가 있는지 검사
            if not os.path.exists(dir_path):
                os.makedirs(dir_path)
                print('dir created')
            print('dir exist')

            # try~except구문으로 이미 폴더가 존재할경우 예외처리
            # try:
            #     os.makedirs(dir_path)
            # except FileExistsError as e:
            #     print('dir exist, error:', e)

            # exist_ok매개변수 추가
            # os.makedirs(dir_path, exist_ok=True)

        def get_img_tag_list():
            """
            디테일페이지에서 img Tag(bs4)의 리스트를 반환
            :return:
            """
            # 디테일 페이지의 html을 가져와 img의 href를 출력
            # print(url_detail)
            # requests를 이용해서 url_detail에 get요청을 보냄
            response = requests.get(url_detail)
            # with open('test.html', 'wt') as f:
            #     f.write(response.text)
            # 응답(Response)에서 .text를 이용해 내용을 가져옴
            # 가져온 응답내용을 이용해 BeautifulSoup인스턴스를 생성 (soup)
            soup = BeautifulSoup(response.text, 'lxml')
            # soup인스턴스에서 select_one메서드를 사용해 웹툰뷰어 태그를 리턴
            div_wt_viewer = soup.select_one('div.wt_viewer')
            # 웹튠뷰어 태그에서 img태그들을 전부 찾아 리스트로 반환
            img_list = div_wt_viewer.find_all('img')
            return img_list

        # 이미지를 다운받을 폴더 생성
        make_episode_dir()

        # 이미지 태그 목록 가져오기
        img_list = get_img_tag_list()

        # 리스트를 순회하며 각 img태그의 src속성을 출력 및 다운로드
        for index, img in enumerate(img_list):
            # 이미지 주소에 get요청
            headers = {'Referer': url_detail}
            response = requests.get(img['src'], headers=headers)

            # 요청 결과 (이미지파일)의 binary데이터를 파일에 쓴다
            img_path = '{}/{:02}.jpg'.format(
                dir_path,
                index
            )
            with open(img_path, 'wb') as f:
                f.write(response.content)

        # 해당 에피소드를 볼 수 있는 HTML파일을 생성
        html_path = './webtoon/{}/{}.html'.format(
            self.webtoon_id,
            episode_num
        )

        html_content = '<html>'
        for index, img in enumerate(img_list):
            html_content += '<img src="./{}/{:02}.jpg">'.format(episode_num, index)
        html_content += '</html>'

        with open(html_path, 'wt') as f:
            f.write(html_content)

        print('Crawling complete')

    def start_scrawler(self):
        pattern_titleID = r'(?<=titleId=)\d*'
        week_list = ['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun']
        while True:
            print('======= 요일별 웹툰 조회 =======\n월요일 : 1\n화요일 : 2\n수요일 : 3\n목요일 : 4\n금요일 : 5\n토요일 : 6\n일요일 : 7\n종료 : 0')
            input_week_num = int(input('======= 조회할 요일의 번호를 입력하세요 : '))
            if type(input_week_num) == int and input_week_num != 0 and input_week_num < 8:
                week = week_list[(input_week_num - 1)]
                response = requests.get('http://comic.naver.com/webtoon/weekdayList.nhn?week=' + week)
                soup = BeautifulSoup(response.text, 'lxml')
                ul_img_list = soup.select_one('ul.img_list')
                dt_list = ul_img_list.find_all('dt')
                webtoon_data_list = [[str(dt.text.strip()), str(dt.find('a')['href'])] for dt in dt_list]

                print('======= 웹툰 리스트 =======')
                print('0 : 돌아가기')
                for index, webtoon_data in enumerate(webtoon_data_list):
                    print(str(index + 1) + ' : ' + str(webtoon_data[0]))

                while True:
                    input_webtoon_num = int(input('======= 웹툰의 번호를 입력하세요 : '))

                    if input_webtoon_num == 0:
                        break
                    elif input_webtoon_num != 0 and not input_webtoon_num > len(webtoon_data_list):
                        m = re.search(pattern_titleID, webtoon_data_list[input_webtoon_num - 1][1])
                        self.webtoon_id = m.group()
                        print('1. 페이지별 웹툰 리스트 조회하기\n2. 에피소드 조회하기\n3. 마지막 에피소드 조회하기\n4. 모든 에피소드 조회하기\n5. 종료')
                        input_view_type = int(input('======= 웹툰 조회 방식을 입력하세요 : '))
                        while True:

                            if input_view_type == 1:
                                page = int(input('에피소드 번호를 입력하세요 : '))
                                self.crawl_page(page)
                                exit()
                            elif input_view_type == 2:
                                episode_num = int(input('에피소드 번호를 입력하세요 : '))
                                self.crawl_episode(episode_num)
                                exit()
                            elif input_view_type == 3:
                                self.crawl_last_episode()
                                exit()
                            elif input_view_type == 4:
                                self.crawl_all_episodes()
                                exit()
                            elif input_view_type == 5:
                                exit()
                            else:
                                self.data_error_msg()
                    else:
                        self.data_error_msg()

            elif input_week_num == 0:
                print('크롤링 시스템을 종료 합니다.')
                break
            else:
                self.data_error_msg()


    @staticmethod
    def data_error_msg():
        print('입력 값이 잘 못 되었습니다.\n 다시 확인하시기 바랍니다.')