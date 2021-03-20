"""
메뉴 만들기
배달 음식 메뉴를 나타낼 클래스 작성
    인스턴스 변수(타입)
        name (문자열) : 메뉴 이름
        price (숫자) : 메뉴 가격
    인스턴스 메소드
        __init__ : MenuItem 클래스의 모든 인스턴스 변수 초기화
        __str__ : MenuItem 인스턴의 정보를 문자열로 리턴
            아래와 같은 형식
            햄버거 가격: 4000
            콜라 가격: 1500
            후렌치 후라이 가격: 1500
"""


class MenuItem:
    # 음식 메뉴를 나타내는 클래스
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return "{} 가격: {}".format(self.name, self.price)


# 메뉴 인스턴스 생성
burger = MenuItem("햄버거", 4000)
coke = MenuItem("콜라", 1500)
fries = MenuItem("후렌치 후라이", 1500)

# 메뉴 인스턴스 출력
print(burger)
print(coke)
print(fries)
