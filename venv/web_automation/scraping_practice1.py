'''
꿈의 직장 전화번호 모으기 1
오렌지 보틀 웹사이트에 가서, 모든 지점의 전화번호 모으기

사이트 : https://workey.codeit.kr/orangebottle/index

모든 지점의 전화번호를 phone_numbers 리스트에 담기
'''

import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook

wb = Workbook(write_only=True)
ws = wb.create_sheet()

ws.append(['지점 이름', '주소', '전화번호'])

response = requests.get("https://workey.codeit.kr/orangebottle/index")
page = response.text
# print(page)

soup = BeautifulSoup(page, 'html.parser')

branch_tags = soup.select('.branch')
# print(tags)

for branch_tag in branch_tags:
    city = branch_tag.select_one('.city').get_text()
    # print(city)
    address = branch_tag.select_one('.address').get_text()
    phoneNum = branch_tag.select_one('.phoneNum').get_text()

    ws.append([city, address, phoneNum])

wb.save('오렌지_보틀.xlsx')