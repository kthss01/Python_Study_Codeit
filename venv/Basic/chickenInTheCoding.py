# 코딩에 빠진 닭
"""
data 폴더의 chicken.txt 파일을 읽어 들이고,
strip과 split을 써서 하루 평균 매출 출력하기
평균을 구하기 위해서는 총 매출을 총 일수로 나누면 됨
"""

with open("data/chicken.txt", "r", encoding="utf-8") as f:
    total_profit = 0
    total_days = 0
    # lines = f.readlines()
    #
    # for line in lines:
    #     datas = line.split(": ")
    #     profit = int(datas[1].strip())
    #     total_profit += profit
    #     total_days += 1

    for line in f:
        data = line.strip().split(": ")
        profit = int(data[1])

        total_profit += profit
        total_days += 1

    print(total_profit / total_days)