# 거스름돈 계산기
"""
가장 적은 수의 지폐로 거스름돈 계산
ex)
    33,000 물건 사기위해 100,000원 지불

    50,000원 1장
    10,000원 1장
    5,000원 1장
    1,000원 2장

calculate_change 함수 구현
payment 지불한 금액을 나타내는 파라미터
cost 물건의 가격을 나타내는 파라마터
"""

moneyFormat = "원 지폐"
countFormat = "장"


def calculate_change(payment, cost):
    change = payment - cost
    money = 50000

    # 50000 계산
    print(f"{money}{moneyFormat}: {change // money}{countFormat}")
    change %= money

    # 10000 계산
    money = 10000
    print(f"{money}{moneyFormat}: {change // money}{countFormat}")
    change %= money

    # 5000 계산
    money = 5000
    print(f"{money}{moneyFormat}: {change // money}{countFormat}")
    change %= money

    # 1000 계산
    money = 1000
    print(f"{money}{moneyFormat}: {change // money}{countFormat}")
    change %= money


def calculate_change2(payment, cost):
    change = payment - cost  # 거스름돈 총액

    fifty_count = change // 50000  # 50,000원 지폐
    ten_count = (change % 50000) // 10000  # 10,000원 지폐
    five_count = (change % 10000) // 5000  # 5,000원 지폐
    one_count = (change % 5000) // 1000  # 1,000원 지폐

    # 답 출력
    print("50000원 지폐: {}장".format(fifty_count))
    print("10000원 지폐: {}장".format(ten_count))
    print("5000원 지폐: {}장".format(five_count))
    print("1000원 지폐: {}장".format(one_count))


# Test
calculate_change(100000, 33000)
print()
calculate_change(500000, 378000)
