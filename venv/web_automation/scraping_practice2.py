'''
꿈의 직장 전화번호 모으기 2
오렌지 보틀 지점의 전화번호에 더해서, 지점 이름(지점이 위치한 도시)와 주소도 모으기

오렌지 보틀의 웹사이트에 가서, 모든 지점의 이름, 주소, 그리고 전화번호를
branch_infos 리스트에 저장

한 지점에 대한 지점 이름, 주소, 전화번호를 리스트 형식으로 추가
branch_infos.append([branch_name, address, phone_number])
'''

import requests
from bs4 import BeautifulSoup

response = requests.get("https://workey.codeit.kr/orangebottle/index")
page = response.text

soup = BeautifulSoup(page, 'html.parser')

branch_infos = []

branch_infos_tags = soup.select('.branch')
# print(branch_infos_tags)
# print(branch_infos_tags[0])
# print(branch_infos_tags[0].select('.city'))
# print(branch_infos_tags[0].select('.city')[0].get_text())

for tag in branch_infos_tags:
    # print(tag)
    branch_name = tag.select_one('.city').get_text()
    address = tag.select_one('.address').get_text()
    phone_number = tag.select_one('.phoneNum').get_text()
    branch_infos.append([branch_name, address, phone_number])

print(branch_infos)
