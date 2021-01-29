# 환전 서비스
"""
가격의 단위 원화인데 미국 달러나 일본 엔화로 얼마일지 확인 원함

krw_to_usd
usd_to_jpy
함수 구현

참고
환율 1달러에 1,000원
1,000엔에 8달러 가정


"""


def krw_to_usd(price):
    return round(price / 1000, 1)


def usd_to_jpy(price):
    return round(price / 8 * 1000, 1)


# 원화
prices = [34000, 13000, 5000, 21000, 1000, 2000, 8000, 3000]

print("한국 화폐: {}".format(prices))

i = 0
while i < len(prices):
    prices[i] = krw_to_usd(prices[i])
    i += 1

print("미국 화폐: {}".format(prices))

i = 0
while i < len(prices):
    prices[i] = usd_to_jpy(prices[i])
    i += 1

print("일본 화폐: {}".format(prices))
