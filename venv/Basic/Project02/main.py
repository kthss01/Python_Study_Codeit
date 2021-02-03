from random import randint, sample

NUMBER_COUNT = 3  # 숫자 야구 뽑기 갯수

# 숫자 3개 뽑기
def generate_numbers():
    numbers = [i for i in range(1, 10)]

    # numbers = []
    #
    # while len(numbers) < 3:
    #     num = randint(0, 9)
    #     if num not in numbers:
    #         numbers.append(num)

    print("0과 9 사이의 서로 다른 숫자 3개를 랜덤한 순서로 뽑았습니다.\n")

    return sample(numbers, 3)
    # return numbers


# print(generate_numbers())


# 숫자 예측하기
def take_guess():
    user_numbers = []

    print("숫자 3개를 하나씩 차례대로 입력하세요.")

    while len(user_numbers) < NUMBER_COUNT:
        user_number = int(input(f"{len(user_numbers)+1}번째 숫자를 입력하세요: "))

        if user_number in user_numbers:
            print("중복되는 숫자입니다. 다시 입력하세요.")
            continue

        if user_number < 0 or user_number > 9:
            print("범위를 벗어나는 숫자입니다. 다시 입력하세요.")
            continue

        user_numbers.append(user_number)

    return user_numbers

    # new_guess = []
    # while len(new_guess) < 3:
    #     new_num = int(input("{}번째 숫자를 입력하세요: ".format(len(new_guess) + 1)))
    #
    #     if new_num < 0 or new_num > 9:
    #         print("범위를 벗어나는 숫자입니다. 다시 입력하세요.")
    #     elif new_num in new_guess:
    #         print("중복되는 숫자입니다. 다시 입력하세요.")
    #     else:
    #         new_guess.append(new_num)
    #
    # return new_guess

# print(take_guess())


# 점수 계산
def get_score(guess, solution):
    # number_cnt = len(guess)
    # strike_cnt, ball_cnt = 0, 0
    #
    # for i in range(number_cnt):
    #     if guess[i] == solution[i]:
    #         strike_cnt += 1
    #     elif guess[i] in solution:
    #         ball_cnt += 1
    #

    strike_count, ball_count = 0, 0

    for i in range(NUMBER_COUNT):
        if guess[i] == solution[i]:
            strike_count += 1
        elif guess[i] in solution:
            ball_count += 1

    return strike_count, ball_count


# 테스트
s_1, b_1 = get_score([2, 7, 4], [2, 4, 7])
print(s_1, b_1)

s_2, b_2 = get_score([7, 2, 4], [2, 4, 7])
print(s_2, b_2)

s_3, b_3 = get_score([0, 4, 7], [2, 4, 7])
print(s_3, b_3)

s_4, b_4 = get_score([2, 4, 7], [2, 4, 7])
print(s_4, b_4)