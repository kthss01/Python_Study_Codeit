# 택이의 우승 상금
"""
우승 상금으로 5,000만원 받음

은행에 맡길 경우 매년 이자 12%
당시 아파트 매개가 5,000만원

현재 아파트 매매가 11억원
1988년 은행에 5,000만원을 넣었을 경우
2016년에 얼마가 있을지 계산하여 어떤게 이득인지 판단하기

은행에 저축해둔 금액이 더 크면
    *원 차이로 동일 아저씨 말씀이 맞습니다.
아파트 가격이 더 크면,
    *원 차이로 미란 아주머니 말씀이 맞습니다.
출력
if문 꼭 사용
"""

money = 5000 * 10000  # 5천만원
rate = 0.12  # 은행 매년 이자
year = 2016 - 1988  # 1988년 ~ 2016년


def calbankbenefit(m, r, y):
    i = 1
    while i <= y:
        m = m + m * r
        i += 1
    return int(m)


bankBenefit = calbankbenefit(money, rate, year)
aptBenefit = 110000 * 10000  # 11억원

# print(bankBenefit)
# print(aptBenefit)

if bankBenefit > aptBenefit:
    print(f"{bankBenefit-aptBenefit}원 차이로 동일 아저씨 말씀이 맞습니다.")
else:
    print(f"{aptBenefit-bankBenefit}원 차이로 미란 아주머니 말씀이 맞습니다.")

##############################################
# 모범 답안

# 상수 정의
INTEREST_RATE = 0.12
APARTMENT_PRICE_2016 = 110000 * 10000

# 변수 정의
year = 1988
bank_balance = 5000 * 10000

while year < 2016:
    bank_balance = bank_balance * (1 + INTEREST_RATE)
    year += 1

if bank_balance > APARTMENT_PRICE_2016:
    print(f"{int(bank_balance-APARTMENT_PRICE_2016)}" /
          f"원 차이로 동일 아저씨 말씀이 맞습니다.")
else:
    print(f"{int(APARTMENT_PRICE_2016-bank_balance)}" /
          f"원 차이로 미란 아주머니 말씀이 맞습니다.")
