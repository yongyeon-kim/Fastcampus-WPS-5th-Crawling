import re
from bs4 import BeautifulSoup
import requests
import urllib.request
import shutil
import os

response = requests.get("http://comic.naver.com/webtoon/list.nhn?titleId=21815&weekday=mon&page=1000")
soup = BeautifulSoup(response.text,'lxml')
print(response.url)
print('564' in response.url)
#
# div = soup.find('div', class_='wt_viewer')
# img_list = div.find_all('img')
#
# test_list = [ img['src'] for img in img_list ]
# print(test_list)



# imgurl = 'http://imgcomic.naver.net/webtoon/21815/564/20170519172310_fdbe88a9cad9efece55d0690f5053681_IMAG01_10.jpg'
#
# filename = imgurl.split("/")[-1]
#
#
#
# response = requests.get(imgurl).content

# with open(filename, 'wb') as f:
#     f.write(response.content)

# directory = './download/'
#
# if not os.path.exists(directory):
#     os.makedirs(directory)
# with open(directory+filename, 'wb') as f:
#     f.write(response)

