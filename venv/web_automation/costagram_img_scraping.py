"""
웹에서 이미지 가져오기
"""

import time
from selenium import webdriver
import requests

# 웹 드라이버 생성 후 코스타그램 접속
driver = webdriver.Chrome("./chromedriver.exe")
driver.implicitly_wait(3)

driver.maximize_window()

driver.get("https://workey.codeit.kr/costagram/index")
time.sleep(1)

# 코스타그램 로그인
driver.find_element_by_css_selector('.top-nav__login-link').click()
time.sleep(1)

driver.find_element_by_css_selector('.login-container__login-input') \
    .send_keys('codeit')
driver.find_element_by_css_selector('.login-container__password-input')\
    .send_keys('datascience')

driver.find_element_by_css_selector('input.login-container__login-button').click()
time.sleep(1)

# 웹 페이지 끝까지 스크롤

# 현재 scrollHeight 가져오기
last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    # scrollHeight까지 스크롤
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # 새로운 내용 로딩될때까지 기다림
    time.sleep(0.5)

    # 새로운 내용 로딩됐는지 확인
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height

# 모든 썸네일 요소 가져오기
posts = driver.find_elements_by_css_selector('.post-list__post')

image_urls = []

for post in posts:
    # 썸네일 클릭
    post.click()
    time.sleep(0.5)

    # 포스트의 이미지 주소를 추출한 다음, 출력
    style_attr = driver.find_element_by_css_selector('.post-container__image')\
        .get_attribute('style')
    image_path = style_attr.split('"')[1]
    image_url = "http://workey.codeit.kr" + image_path
    image_urls.append(image_url)

    # 닫기 버튼 클릭
    driver.find_element_by_css_selector('.close-btn').click()
    time.sleep(0.5)

# 웹 드라이버 종료
driver.quit()

# 이미지 다운로드
for i in range(len(image_urls)):
    image_url = image_urls[i]
    response = requests.get(image_url)
    filename = './images/image{}.jpg'.format(i)
    with open(filename, 'wb+') as f:
        f.write(response.content)
