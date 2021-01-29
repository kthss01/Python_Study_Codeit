# 약수 찾기
"""
정수 n의 약수는 n을 나누었을 때 나누어 떨어지는 수
만약 정수 i가 정수 n의 약수라면,
n을 i로 나누었을 때 나머지가 0이 나와야 함

정수 120의 약수 모두 출력하고 총 몇개의 약수가 있는지 출력
"""


def find_divisor(num):
    cnt = 0

    i = 1
    while i <= num:
        if num % i == 0:
            cnt += 1
            print(i)
        i += 1

    return "{}의 약수는 총 {}개입니다.".format(num, cnt)


print(find_divisor(120))
