import re
import requests

# url = 'http://comic.naver.com/webtoon/list.nhn?titleId=662774&weekday=wed'

# 실제 요청한 URL(URL과 Params가 합쳐진을 print 해보기
# print(무언) -> 위의 url과 params를 조합해서 만들어질 요청URL을 출력
# 위의 두 변수(url, params)는 사용하면 안됨. requests라이브러리가 지원하는 방식으로 해결

url = 'http://comic.naver.com/webtoon/list.nhn?'
params = {'titleId': '662774', 'weekday': 'wed', 'page':'1'}

response = requests.get(url, params=params)
print(type(response))
print('URL : ' + response.url)
# print(html.text)

# 응답의 상태코드 출력
print('Response Code : ' + str(response.status_code))

# 응답의 텍스트 인코딩을 출력
# print('Encoding : ' + response.encoding)


# 이 작업들을 한 번에 처리해주는 함수를 구현
def get_html_from_url(url, params):
    html = requests.get(url, params)
    return html.text

html = get_html_from_url(url,params)

print( html )




    # try:
    #     pattern = r'http://thumb.comic.naver.net/webtoon/662774/'
    #     source = html.text
    #
    #     m_list = re.finditer(pattern, source)
    #     result_list = [m.group() for m in m_list]
    #
    # except Exception as e:
    #     print(e)
    # else:
    #     print(result_list)


    # http://thumb.comic.naver.net/webtoon/662774/89/thumbnail_202x120_43ea169c-3b0e-414b-b54f-386dbfde116a.jpg

    # with open('webtoon.html','wt') as f:
    #    f.write(r.text)
