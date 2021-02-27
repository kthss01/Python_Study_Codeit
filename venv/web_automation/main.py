# 라이브러리
# 유용한 기능을 제공함
# os, datetime, shutil 스탠다드 모듈

'''
TV 시청률 데이터 가져오기
티비랭킹닷컴의 HTML 코드를 rating_page에 저장하기
'''

import requests
from bs4 import BeautifulSoup

# response = requests.get("https://google.com")
# print(response)  # 성공하면 200 실패하면 500
# print(response.text)

# response = requests.get("https://workey.codeit.kr/ratings/index")
# rating_page = response.text

# 출력 코드
# print(rating_page)

# rating_pages = []
# # https://workey.codeit.kr/ratings/index?year=2010&month=1&weekIndex=0
# for i in range(5):
#     url = "https://workey.codeit.kr/ratings/index?year=2010&month=2&weekIndex={}".format(i)
#     # print(url)
#     response = requests.get(url)
#     rating_page = response.text
#     rating_pages.append(rating_page)
#
# print(len(rating_pages))
# print(rating_pages[4])

'''
TV 시청률 데이터 가져오기 2
티비랭킹닷컴 사이트에서 모든 기간의 데이터 가져오기
모든 페이지의 HTML 코드를 rating_pages에 저장
2010년 1월부터 2018년 12월까지 모든 달에 대해, 
1주차 ~ 5주차 페이지를 순서대로 리스트에 저장
5주차가 없는 달은 데이터가 없는 페이지로 나오는데. 그런 페이지도 리스트에 넣기
'''

# https://workey.codeit.kr/ratings/index?year=2010&month=1&weekIndex=0
# rating_pages = []
#
# for year in range(2010, 2019):
#     for month in range(1, 13):
#         for week in range(0, 5):
#             url = f"https://workey.codeit.kr/ratings/index?year={year}&month={month}&weekIndex={week}"
#             response = requests.get(url)
#             rating_page = response.text
#             rating_pages.append(rating_page)
#
# # 출력 코드
# print(len(rating_pages)) # 가져온 총 페이지 수
# print(rating_pages[0]) # 첫 번째 페이지의 HTML 코드

# response = requests.get("https://workey.codeit.kr/music")
# music_page = response.text
#
# soup = BeautifulSoup(music_page, 'html.parser')
#
# # print(soup.select('ul.popular__order li'))
#
# popular_artists = []
#
# for tag in soup.select('ul.popular__order li'):
#     # print(tag.get_text().strip())
#     # popular_artists.append(tag.get_text().strip())
#
#     # print(list(tag.strings))
#     # print(list(tag.stripped_strings)[1])
#     popular_artists.append(list(tag.stripped_strings)[1])
#
# print(popular_artists)

# response = requests.get('https://workey.codeit.kr/ratings/index')
# rating_page = response.text
# #
# # # print(rating_page)
# #
# soup = BeautifulSoup(rating_page, 'html.parser')
#
# # print(soup.prettify())
# # print(soup.select('title'))
# # print(soup.select('table'))
# # print(soup.select('td.program'))
#
# program_title_tags = soup.select('td.program')
#
# # program_titles = []
# #
# # for tag in program_title_tags:
# #     # print(tag.get_text())
# #     program_titles.append(tag.get_text())
# #
# # print(program_titles)
#
# print(soup.select_one('td.program'))

# print(soup.select('td')[:4])
# td_tags = soup.select('td')[:4]
#
# for tag in td_tags:
#     print(tag.get_text())

# # print(soup.select('tr')[1])
# tr_tag = soup.select('tr')[1]
# # td_tags = tr_tag.select('td')
# td_tags = tr_tag.select('*')
# print(td_tags)
#
# for tag in td_tags:
#     print(tag.get_text())

response = requests.get('https://workey.codeit.kr/ratings/index')
rating_page = response.text

soup = BeautifulSoup(rating_page, 'html.parser')

# print(soup.select_one('img')['src'])
print(soup.select_one('img').attrs)
