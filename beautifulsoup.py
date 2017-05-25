import re
from bs4 import BeautifulSoup
import requests

# url = 'http://comic.naver.com/webtoon/list.nhn?titleId=662774&weekday=wed'

# 실제 요청한 URL(URL과 Params가 합쳐진을 print 해보기
# print(무언) -> 위의 url과 params를 조합해서 만들어질 요청URL을 출력
# 위의 두 변수(url, params)는 사용하면 안됨. requests라이브러리가 지원하는 방식으로 해결

url = 'http://comic.naver.com/webtoon/list.nhn?'
params = {'titleId': '662774', 'weekday': 'wed', 'page':'1'}

response = requests.get(url, params=params)
# print(html.text)

# 이 작업들을 한 번에 처리해주는 함수를 구현
def get_html_from_url(url, params):
    html = requests.get(url, params)
    return html.text

html = get_html_from_url(url,params)
soup = BeautifulSoup(html, "lxml")

div_comicinfo = soup.find('div', class_='comicinfo')
div_comicinfo_detail = div_comicinfo.find('div', class_='detail')
div_comicinfo_detail_h2 = div_comicinfo_detail.find('h2')

title = div_comicinfo_detail_h2.contents[0].strip()
print(title)

div_comicinfo_detail_h2_wrt_nm = div_comicinfo_detail_h2.find('span', class_='wrt_nm')
auther_name = div_comicinfo_detail_h2_wrt_nm.text.strip()
print(auther_name)

print('------------------------------------------------')

# 에피소드 리스트를 가져온다
# 각 에피소드는 class Episode형 인스턴스가 되도록 함
# 각 에피소드의 썸네일 이미지 URL, 제목, 별점 등록일을
# url_thumbnail, title, rating, date에 등록

# tr_list = soup.select('table.viewList > tr')
# css 방식은 문서에서 selector로 검색해 볼 것.

table = soup.find('table', class_='viewList')
tr_list = table.find_all('tr')

for tr in tr_list:
    if not tr.find('td', class_='title'):
        continue
    title = tr.find('td', class_='title').find('a').text
    link = tr.find('td', class_='title').find('a').text
    rating = tr.find_all('td')[2].find('strong').text

    print(title)
    print(link)


"""
['\n', <td>
<a href="/webtoon/detail.nhn?titleId=662774&amp;no=80&amp;weekday=wed" onclick="clickcr(this,'lst.img','662774','80',event)">
<img alt="78화 - 들개 무리(20화)" height="41" onerror="this.src='http://static.comic.naver.net/staticImages/COMICWEB/NAVER/img/common/non71_41.gif'" src="http://thumb.comic.naver.net/webtoon/662774/8bnail_202x120_31ba6dd8-94fe-4f64-a153-f9caa4d77819.jpg" title="78화 - 들개 무리(20화)" width="71"/>
<span class="mask"></span>
</a>
</td>, '\n', <td class="title">
<a href="/webtoon/detail.nhn?titleId=662774&amp;no=80&amp;weekday=wed" onclick="clickcr(this,'lst.title','662774','80',event)">78화 - 들개 무리(20화)</a>
</td>, '\n', <td>
<div class="rating_type">
<span class="star"><em style="width:99.78%">평점</em></span>
<strong>9.98</strong>
</div>
</td>, '\n', <td class="num">2017.03.07</td>, '\n']
"""




class Episode:

    def __init__(self, url_thumbnail, title, rating, date):
        self.url_thumbnail = url_thumbnail
        self.title = title
        self.rating = rating
        self.date = date




    pass



episode_list = []










