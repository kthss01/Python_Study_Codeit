"""
Selenium 기능 더 알아보기: 웹 브라우저 제어하기
"""

import time
from selenium import webdriver

driver = webdriver.Chrome("./chromedriver.exe")
driver.implicitly_wait(3)

# driver.maximize_window()

# 쿠팡 '커피' 검색 결과 페이지 접속
driver.get('https://www.coupang.com/np/search?component=&q=%EC%BB%A4%ED%94%BC&channel=user')
time.sleep(1)

products = driver.find_elements_by_css_selector('li.search-product')

# 검색 결과 페이지로 계속 돌아올 것이기 때문에 저장해 놓기
search_result_window = driver.current_window_handle

for product in products:
    # 아이템 클릭
    product.click()
    time.sleep(1)

    # 아이템 상세 페이지로 포커스 이동
    driver.switch_to.window(driver.window_handles[1])
    time.sleep(1)

    # 아이템 상세 페이지에서 필요한 정보 가져오기

    # 아이템 상세 페이지 닫기
    driver.close()

    # 검색 결과 페이지로 포커스 이동 - 그래야 아이템 (product)를 클릭 할 수 있음
    driver.switch_to.window(search_result_window)

driver.quit()
