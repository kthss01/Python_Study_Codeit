# 로또 시뮬레이션

from random import sample, randint


# 번호 뽑기
def generate_numbers(n):
    lotto_nums = [i for i in range(1, 46)]
    return sample(lotto_nums, n)


# 당첨 번호 뽑기
def draw_winning_numbers():
    winning_numbers = generate_numbers(7)
    return sorted(winning_numbers[:6]) + winning_numbers[6:]


# 겹치는 번호 개수
def count_matching_numbers(list_1, list_2):
    return len(set(list_1).intersection(list_2))


# 당첨금 확인
"""
    규칙
    1. 6 == 6 (10억 원)
    2. 5 == 5 , 1 == 보너스 번호 (5천만 원) 
    3. 5 == 5 (100만 원) 
    4. 4 == 4 (5만 원) 
    5. 3 == 3 (5천 원) 
"""
def check(numbers, winning_numbers):
    winning_money = {
        6 : 50000 * 10000,
        5.5 : 5000 * 10000,  # 보너스 번호
        5 : 100 * 10000,
        4 : 5 * 10000,
        3 : 5 * 1000
    }

    count = count_matching_numbers(numbers, winning_numbers[:6])
    bonus_count = count_matching_numbers(numbers, winning_numbers[6:])

    if count == 5 and bonus_count == 1:
        count += 0.5

    if count <= 2:
        return 0
    else:
        return winning_money[count]


