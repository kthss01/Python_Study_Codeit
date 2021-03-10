"""
꿈의 직장 전화번호 모으기 4
꿈의 직장 전화번호 모으기 2 과제에서 했던 작업을
Selenium을 써서 해보기기
"""

import time
from selenium import webdriver

driver = webdriver.Chrome('./chromedriver.exe')

driver.get("https://workey.codeit.kr/orangebottle/index")
time.sleep(1)

branch_infos = []

# branches = driver.find_elements_by_css_selector('div.branch')
#
# for branch_element in branches:
#     branch_name = branch_element.find_element_by_css_selector('p.city').text
#     address = branch_element.find_element_by_css_selector('p.address').text
#     phone_number = branch_element.find_element_by_css_selector('span.phoneNum').text
#     branch_infos.append([branch_name, address, phone_number])

for branch in driver.find_elements_by_css_selector('div.branch p'):
    branch_infos.append(branch.text.strip())

driver.quit()

print(branch_infos)

