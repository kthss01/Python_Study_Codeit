import time
from selenium import webdriver
# from selenium.webdriver.chrome.options import Options

# options = Options()
# options.add_argument('--start-fullscreen')

driver = webdriver.Chrome('./chromedriver.exe')
# driver = webdriver.Chrome(executable_path='./chromedriver.exe', chrome_options=options)
driver.implicitly_wait(3)

# driver.set_window_size(1024, 640)
driver.maximize_window()

driver.get('https://workey.codeit.kr/music')
time.sleep(3)

# driver.execute_script("window.scrollTo(0, 200);")
#
# scroll_height = driver.execute_script("return document.body.scrollHeight;")
# print(scroll_height)

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

