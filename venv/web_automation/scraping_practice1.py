'''
꿈의 직장 전화번호 모으기 1
오렌지 보틀 웹사이트에 가서, 모든 지점의 전화번호 모으기

사이트 : https://workey.codeit.kr/orangebottle/index

모든 지점의 전화번호를 phone_numbers 리스트에 담기
'''

import requests
from bs4 import BeautifulSoup

response = requests.get("https://workey.codeit.kr/orangebottle/index")
page = response.text
# print(page)

soup = BeautifulSoup(page, 'html.parser')

# phone_numbers_tags = soup.select('span.phoneNum')
phone_numbers_tags = soup.select('.phoneNum')
phone_numbers = []

for tag in phone_numbers_tags:
    phone_numbers.append(tag.get_text())

print(phone_numbers)
