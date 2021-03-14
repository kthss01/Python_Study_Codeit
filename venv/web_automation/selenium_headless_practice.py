"""
Selenium 기능 더 알아보기: Headless 모드
"""

import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--headless")
options.add_argument("window-size=1920,1080")

driver = webdriver.Chrome('./chromedriver.exe', options=options)
driver.implicitly_wait(3)

driver.get('https://workey.codeit.kr/music')

driver.quit()
