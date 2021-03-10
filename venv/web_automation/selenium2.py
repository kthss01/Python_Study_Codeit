import time
from selenium import webdriver

driver = webdriver.Chrome('./chromedriver.exe')
driver.implicitly_wait(3)  # 페이지 로딩이 완료되기까지 몇초 기다릴지 정하는거

driver.get('https://workey.codeit.kr/costagram/index')

# beautiful soup select_one 과 같음
# driver.find_element_by_css_selector('.top-nav__login-link').click()
# driver.find_element_by_css_selector('.login-container__login-input').send_keys('codeit')
# driver.find_element_by_css_selector('.login-container__password-input').send_keys('datascience')
#
# driver.find_element_by_css_selector('.login-container__login-button').click()

# time.sleep(5)  # 5초간 멈춤
time.sleep(1)

# 크롬 개발자 도구에서 copy selector 로 가져오기
driver.find_element_by_css_selector('#app > nav > div > a').click()

time.sleep(1)
driver.find_element_by_css_selector('#app > div > div > div > form > input.login-container__login-input').send_keys('codeit')
driver.find_element_by_css_selector('#app > div > div > div > form > input.login-container__password-input').send_keys('datascience')

driver.find_element_by_css_selector('#app > div > div > div > form > input.login-container__login-button').click()

