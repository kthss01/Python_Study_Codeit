"""
코스타그램 스크래핑 2
    각 포스트의 이미지 주소를 추출한 다음, 출력 해주는 코드 추가
"""

import time
from selenium import webdriver

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

for post in posts:
    # 썸네일 클릭
    post.click()
    time.sleep(0.5)

    # 포스트의 이미지 주소를 추출한 다음, 출력
    style_attr = driver.find_element_by_css_selector('.post-container__image')\
        .get_attribute('style')
    # print(style_attr)
    # print(type(style_attr))
    # bg_img = style_attr.split(";")[0].strip()
    # post_img = bg_img[bg_img.find("url")+5:-2]  # url(" : ") 까지 하기 위해 5:-2 슬라이싱
    # print(post_img)
    image_url = style_attr.split('"')[1]
    print(image_url)

    # 닫기 버튼 클릭
    driver.find_element_by_css_selector('.close-btn').click()
    time.sleep(0.5)

# 웹 드라이버 종료
driver.quit()
