# range 연습
"""
numbers 리스트
for문 과 range함수를 사용하여, numbers의 인덱스와 원소 출력
"""

numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]

# 인덱스와 원소 출력
# 코드를 입력하세요.

for i in range(len(numbers)):
    print("{} {}".format(i, numbers[i]))