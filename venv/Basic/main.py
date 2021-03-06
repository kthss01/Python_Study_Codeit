print("Hello Python For Codeit")

# 한 줄 주석
''' 여러 줄 주석  '''
""" 여러 줄 주석 """


def hello():
    print("Welcome to Codeit!")


hello()
hello()
hello()

print(round(3.141592, 4))

year, month, day = 2019, 10, 29
date_string = "오늘은 {1}년 {0}월 {2}일입니다."
print(date_string.format(month, year, day))

print(True and False)


def temp():
    print("temp")


print(temp())

a = 10


def test():
    global a
    a = 5
    print("local {}".format(a))


test()
print("global {}".format(a))

my_dictionary = {
    5: 25,
    2: 4,
    3: 9
}
print(my_dictionary[3])
my_dictionary[9] = 81

import datetime

# datetime 값 생성
pi_day = datetime.datetime(2021, 2, 2)
pi_day = datetime.datetime(2021, 2, 2, 21, 2, 00)
print(pi_day)
print(type(pi_day))

today = datetime.datetime.now()
print(today)
print(type(today))

# 두 datetime 값 사이의 기간을 알고 싶으면 빼면 됨
timedelta = today - pi_day
print(timedelta)
print(type(timedelta))

my_timedelta = datetime.timedelta(days=5, hours=3, minutes=10,seconds=50)
print(today + my_timedelta)

print(today.year)  # 연도
print(today.month)  # 월
print(today.day)  # 일
print(today.hour)  # 시
print(today.minute)  # 분
print(today.second)  # 초
print(today.microsecond)  # 마이크로초

# datetime 포맷팅
print(today.strftime("%A, %B %dth %Y"))  #%A, %B, %d, %Y 포캣 코드

# 파일 쓰기
import random
f = open('test.txt', 'w', encoding="utf-8")

for i in range(1, 11):
    data = "{}일차 : {}원\n".format(i, random.randint(1000 * i, 10000 * i))
    f.write(data)

f.close()  # with문으로 쓰면 close 할 필요가 없음

with open('test.txt', 'r', encoding='utf-8') as f:
    # print(f.read())

    # lines = f.readlines()
    # for line in lines:
    #     print(line.strip('\n'))

    line = None
    while line != '':
        line = f.readline()
        print(line.strip('\n'))  # 파일에서 읽어온 문자열에서 \n 삭제하여 출력

print(" \ta  b\n\n".strip())

my_string = "1. 2. 3. 4. 5. 6"
print(my_string.split("."))  # 이렇게만 하면 띄어쓰기만 남음
print(my_string.split(". "))  # strip활용하거나 '. ' 이걸로 split