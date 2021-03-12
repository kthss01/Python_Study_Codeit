"""
코스타그램 스크래핑 3
    코스타그램 스크래핑 마무리
    '코스타그램.xlsx' (또는 '코스타그램.csv') 라는 이름으로 엑셀 파일을 만들어 주세요.
    파일의 헤더 행은 '이미지 주소', '내용', '해시태그', '좋아요 수', '댓글 수'로 작성
    이미지 주소에 이어서, 각 포스팅의 내용, 해시태그들, 좋아요 수, 댓글 수를 가져온
    다음 엑셀 파일에 저장해 주세요 (이미지 주소를 출력하는 코드는 지워주세요)
"""

import time
from selenium import webdriver
from openpyxl import Workbook

wb = Workbook(write_only=True)
ws = wb.create_sheet()

ws.append(['이미지 주소', '내용', '해시태그', '좋아요 수', '댓글 수'])

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
driver.find_element_by_css_selector('.login-container__password-input') \
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

for post in posts:
    # 썸네일 클릭
    post.click()
    time.sleep(0.5)

    # 포스트의 이미지 주소를 추출
    style_attr = driver.find_element_by_css_selector('.post-container__image') \
        .get_attribute('style')
    image_url = style_attr.split('"')[1]

    # 내용
    text = driver.find_element_by_css_selector('.content__text').text.strip()

    # 해시태그
    hashtags = driver.find_element_by_css_selector('.content__tag-cover').text.strip()

    # 좋아요 수
    like_count = driver.find_element_by_css_selector('.content__like-count').text.strip()

    # 댓글 수
    comment_count = driver.find_element_by_css_selector('.content__comment-count').text.strip()

    # print("{}\n{}\n{}\n{}\n{}".format(image_url, text, tags, like_count, comment_count))
    ws.append([image_url, text, hashtags, like_count, comment_count])

    # 닫기 버튼 클릭
    driver.find_element_by_css_selector('.close-btn').click()
    time.sleep(0.5)

# 웹 드라이버 종료
driver.quit()

wb.save('코스타그램.xlsx')
