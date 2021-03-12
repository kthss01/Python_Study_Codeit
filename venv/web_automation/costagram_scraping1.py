"""
코스타그램 스크래핑 1
    웹 드라이버 생성 후 코스타그램 (https://workey.codeit.kr/costagram/index) 접속
    코스타그램 로그인
    웹 페이지 끝까지 스크롤
    각 썸네일(포스팅)을 클릭하고, 창이 뜨면 닫기 버튼 누르기
    웹 드라이버 종료
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
driver.find_element_by_css_selector('#app > nav > div > a').click()
time.sleep(1)

driver.find_element_by_css_selector('#app > div > div > div > form > input.login-container__login-input') \
    .send_keys('codeit')
driver.find_element_by_css_selector('#app > div > div > div > form > input.login-container__password-input')\
    .send_keys('datascience')
driver.find_element_by_css_selector('#app > div > div > div > form > input.login-container__login-button').click()
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

# 각 썸네일(포스팅)을 클릭하고, 창이 뜨면 닫기 버튼 누르기
# thumbnails = driver.find_elements_by_css_selector('div.post')
# # print(thumbnails)
#
# # thumbnails[2].click()
# # time.sleep(1)
# # print(driver.find_element_by_css_selector('.close-btn').is_enabled())
#
# # 자바스크립트로 실행 시키는 법 모달창이 웹페이지 창보다 크면 이렇게 해결
# # element = driver.find_element_by_css_selector('.close-btn')
# # driver.execute_script("arguments[0].click();", element)
#
# for thumbnail in thumbnails:
#     thumbnail.click()
#     time.sleep(0.5)
#     driver.find_element_by_css_selector('#app > div > div > div > button').click()
#     time.sleep(0.5)

# 모든 썸네일 요소 가져오기
posts = driver.find_elements_by_css_selector('.post-list__post')

for post in posts:
    # 썸네일 클릭
    post.click()
    time.sleep(0.5)

    # 닫기 버튼 클릭
    driver.find_element_by_css_selector('.close-btn').click()
    time.sleep(0.5)

# 웹 드라이버 종료
driver.quit()
