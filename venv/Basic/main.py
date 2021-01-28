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
