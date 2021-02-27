'''
검색어 순위 받아오기
음악 사이트의 검색어 순위 받아오기
'인기 아티스트' 아래에 있는 '검색어 순위'의 1위 ~ 10위 데이터
popular_searches 리스트에 담기
순위, 순위 변동을 제외한 검색어만 담기

https://workey.codeit.kr/music
'''

import requests
from bs4 import BeautifulSoup

response = requests.get("https://workey.codeit.kr/music")
page = response.text

soup = BeautifulSoup(page, 'html.parser')
# print(soup)

# print(soup.select('ul.rank__order li'))

popular_searches = []

for tag in soup.select('ul.rank__order li'):
    # print(list(tag.stripped_strings)[2])
    popular_searches.append(list(tag.stripped_strings)[2])

print(popular_searches)
