# 로또 시뮬레이션

from random import sample, randint


# 번호 뽑기
def generate_numbers(n):
    lotto_nums = [i for i in range(1, 46)]
    # print(lotto_nums)
    return sample(lotto_nums, n)

    # numbers = []
    # while len(numbers) < n:
    #     num = randint(1, 45)
    #     if num not in numbers:
    #         numbers.append(num)
    #
    # return numbers

# print(generate_numbers(6))
# print(generate_numbers(7))


# 당첨 번호 뽑기
def draw_winning_numbers():
    # nums = generate_numbers(7)
    # normal_nums, bonus_num = nums[:6], nums[-1]
    # normal_nums.sort()
    # nums = normal_nums
    # nums.append(bonus_num)
    # return nums

    winning_numbers = generate_numbers(7)
    return sorted(winning_numbers[:6]) + winning_numbers[6:]

# print(draw_winning_numbers())


# 겹치는 번호 개수
def count_matching_numbers(list_1, list_2):
    # count = 0
    # for element in list_1:
    #     if element in list_2:
    #         count += 1
    # return count

    return len(set(list_1).intersection(list_2))


# print(count_matching_numbers([2, 7, 11, 14, 25, 40], [2, 11, 13, 14, 30, 35]))
# print(count_matching_numbers([2, 7, 11, 14, 25, 40], [14]))


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
    #
    # count = len(set(numbers).intersection(winning_numbers[:6]))
    # if count == 5 and winning_numbers[-1] in numbers:
    #     count += 0.5
    #
    # return winning_money[count]

    count = count_matching_numbers(numbers, winning_numbers[:6])
    bonus_count = count_matching_numbers(numbers, winning_numbers[6:])

    if count <= 2:
        return 0
    else:
        return winning_money[count]

print(check([2, 4, 11, 14, 25, 40], [4, 12, 14, 28, 40, 41, 6]))
print(check([2, 4, 11, 14, 25, 40], [2, 4, 10, 11, 14, 40, 25]))


