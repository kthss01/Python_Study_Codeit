# 단어 퀴즈
"""
vocabulary.txt라는 파일을 이용해 문제를 내는 프로그램 만들기
콘솔에 한국어 뜻을 알려주고
사용자는 그에 맞는 영어 단어를 입력

영어 단어가 정답이면  "맞았습니다!"
틀리면 "아쉽습니다. 정답은 000입니다." 출력

문제를 내는 순서는 vocabulary.txt에 정리된 순서
"""

with open("data/vocabulary.txt", "r", encoding="utf-8") as f:
    for line in f:
        # eng_word, kor_word = line.strip().split(": ")  # 이것도 좋은데 위험할 수 있음
        data = line.strip().split(": ")
        eng_word, kor_word = data[0], data[1]
        # print("{} {}".format(eng_word, kor_word))

        quiz = input("{}: ".format(kor_word))
        if quiz == eng_word:
            print("맞았습니다!")
        else:
            print("아쉽습니다. 정답은 {}입니다.".format(eng_word))