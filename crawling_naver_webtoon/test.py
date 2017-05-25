import re
from bs4 import BeautifulSoup
import requests
import urllib.request
import shutil

# response = requests.get("http://comic.naver.com/webtoon/detail.nhn?titleId=21815&no=564&weekday=mon")
# soup = BeautifulSoup(response.text,'lxml')
#
# div = soup.find('div', class_='wt_viewer')
# img_list = div.find_all('img')
#
# test_list = [ img['src'] for img in img_list ]
# print(test_list)



imgurl = 'http://imgcomic.naver.net/webtoon/21815/564/20170519172310_fdbe88a9cad9efece55d0690f5053681_IMAG01_10.jpg'

filename = imgurl.split("/")[-1]



response = requests.get(imgurl, stream=True)

# with open(filename, 'wb') as f:
#     f.write(response.content)


with open(filename, "wb") as f:
    for chunk in response.iter_content(chunk_size=1024):

        # writing one chunk at a time to pdf file
        if chunk:
            f.write(chunk)