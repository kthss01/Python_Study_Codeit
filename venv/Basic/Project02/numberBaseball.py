from random import randint, sample

NUMBER_COUNT = 3  # 숫자 야구 뽑기 갯수

# 숫자 3개 뽑기
def generate_numbers():
    numbers = [i for i in range(1, 10)]

    print("0과 9 사이의 서로 다른 숫자 3개를 랜덤한 순서로 뽑았습니다.\n")

    return sample(numbers, NUMBER_COUNT)


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


# 점수 계산
def get_score(guess, solution):
    strike_count, ball_count = 0, 0

    for i in range(NUMBER_COUNT):
        if guess[i] == solution[i]:
            strike_count += 1
        elif guess[i] in solution:
            ball_count += 1

    return strike_count, ball_count


ANSWER = generate_numbers()
tries = 0

while True:
    guess = take_guess()

    s, b = get_score(guess, ANSWER)

    print("{}S {}B\n".format(s, b))

    tries += 1

    if s == NUMBER_COUNT:
        break

print("축하합니다. {}번 만에 숫자 {}개의 값과 위치를 모두 맞추셨습니다.".format(tries, NUMBER_COUNT))