# 단어장 만들기
"""
콘솔로 영어 단어와 한국어 뜻을 받고
vocabulary.txt라는 새로운 텍스트 파일에 단어와 뜻 정리
사용자가 새로운 단어와 뜻을 입력할 때마다 작성

사용자가 단어나 뜻으로 q를 입력한 순간 프로그램 즉시 종료
사용자가 q를 입력하고나면 파일은 더 이상 바뀌지 않아야함
"""

# 파일 여는 부분이 맨 위에 있는게 맞는거 같음 그래야 열고 닫는게 반복이 안됨
with open("data/vocabulary.txt", "a", encoding="utf-8") as f:
    while True:
        eng_word = input("영어 단어를 입력하세요: ")
        if eng_word == 'q':
            break

        kor_word = input("한국어 뜻을 입력하세요: ")
        if kor_word == 'q':
            break

    # with open("data/vocabulary.txt", "a", encoding="utf-8") as f:
        f.write("{}: {}\n".format(eng_word, kor_word))