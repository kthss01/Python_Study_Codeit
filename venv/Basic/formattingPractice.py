# 문자열 포맷팅 연습
"""
wage 1시간에 얼마 버는지를 나타내는 값
exchange_rate 환율(1달러 -> 한국 돈으로 얼마)
wage * 1 1시간 동안 번 금액
wage * 1 * exchange_rate 1시간 동안 번 금액 환전

문자열 포맷팅의 개념을 이용하여 문장 출력
"""

wage = 5 # 시급
exchange_rate = 1142.16 # 환율


def wage_hour(hour):
    return wage * hour


def kor_wage_hour(hour):
    return wage * hour * exchange_rate


money_format = "달러"
time = 1
print("{}시간에 {}{} 벌었습니다.".format(time, wage_hour(time), money_format))
time = 5
print(f"{time}시간에 {wage_hour(time)}{money_format} 벌었습니다.")
time = 1
money_format = "원"
print("{}시간에 {}{} 벌었습니다.".format(time, kor_wage_hour(time), money_format))
time = 5
print("{}시간에 {:.1f}{} 벌었습니다.".format(time, kor_wage_hour(time), money_format))
