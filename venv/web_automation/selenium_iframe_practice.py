"""
Selenium 기능 더 알아보기: iframe 다루기
"""

import time
from selenium import webdriver

driver = webdriver.Chrome('./chromedriver.exe')
driver.implicitly_wait(3)

# 코드잇 네이버 블로그 접속
driver.get('https://blog.naver.com/codeitofficial')
time.sleep(1)

# 'mainFrame'으로 이동
driver.switch_to.frame('mainFrame')

# 블로그 글 내용 출력
print(driver.find_element_by_css_selector('div.se-main-container').text)

driver.quit()
