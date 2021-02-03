# 고급 단어장
"""
단어 퀴즈 프로그램과 같이 만들되
이번엔 random 모듈과 사전(dictionary)을 이용해서
vocabulary.txt의 단어들을 랜덤한 순서로 내도록 프로그램 변경

같은 단어를 여러번 물어봐도 괜찮고, 프로그램은 사용자가 알파벳 q를 입력할 때까지 계속 실행
"""

import random

wordbook = {}

with open("data/vocabulary.txt", "r", encoding="utf-8") as f:
    for line in f:
        datas = line.strip().split(": ")
        eng_word, kor_word = datas[0], datas[1]
        # wordbook[kor_word] = eng_word
        wordbook[eng_word] = kor_word

# print(wordbook)
# print(len(wordbook))

# 문제 내기
while True:
    # num = random.randint(0, len(wordbook)-1)
    # problem = list(wordbook.keys())[num]
    # answer = input("{}: ".format(problem))
    #
    # if answer == 'q':
    #     break
    #
    # if answer == wordbook[problem]:
    #     print("맞았습니다!")
    # else:
    #     print("틀렸습니다. 정답은 {}입니다.".format(wordbook[problem]))

    # 랜덤한 문제 받아오기
    keys = list(wordbook.keys())
    # index = random.randint(0, len(keys) - 1)
    # eng_word = keys[index]
    eng_word = random.choice(keys)

    kor_word = wordbook[eng_word]

    # 유저 입력값 받기
    guess = input("{}: ".format(kor_word))

    # 프로그램 끝내기
    if guess == 'q':
        break

    # 정답 확인하기
    if guess == eng_word:
        print("정답입니다!")
    else:
        print("틀렸습니다. 정답은 {}입니다.".format(eng_word))
