# 숫자 맞히기 게임
"""
1 과 20 사이의 숫자 맞히기 게임
random 모듈과 input 함수 활용

진행방식
    1. "기회가 *번 남았스니다. 1 ~ 20 사이의 숫자를 맞혀 보세요: " 출력
    총 네번의 기회가 주어지며, 사용자가 한 번 추측할 때마다 남은 기회 횟수가 줄어듬
    2. 정답을 맞히면 "축하합니다. *번 만에 숫자를 맞히셨습니다." 출력되고 프로그램 종료
    3. 사용자가 입력한 수가 정답보다 작은 경우 "Up" 출력
    큰 경우 "Down" 출력
    4. 정답이 틀렸으면 1번부터 다시 진행.
    네번의 기회를 모두 사용했는데도 답을 맞히지 못했으면,
    "아쉽습니다. 정답은 *입니다." 출력되고 프로그램 종료
"""

import random

ANSWER = random.randint(1, 20)
NUM_TRIES = 4

while True:
    guess = int(input("기회가 {}번 남았습니다. 1-20 사이의 숫자를 맞혀보세요: ".format(NUM_TRIES)))

    if ANSWER == guess:
        print("축하합니다. {}번 만에 숫자를 맞히셨습니다.".format(NUM_TRIES))
        break
    elif ANSWER > guess:
        print("Up")
    else:
        print("Down")

    NUM_TRIES -= 1
    if NUM_TRIES == 0:
        print("아쉽습니다. 정답은 {}입니다.".format(ANSWER))
        break