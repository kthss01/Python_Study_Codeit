# 피보나치 수열
"""
피보나치 수열 (Fibonacci Sequence)
    1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ...
수열 1항, 2항은 각각 1
3번 항부터는 바로 앞 두 항의 합으로 계산

피보나치 수열의 첫 50개 항을 차례대로 출력
"""


# # 재귀 함수 방법인데 너무 오래 걸림
# def fibo(num):
#     if num == 1 or num == 2:
#         return 1
#     return fibo(num - 1) + fibo(num - 2)
#
#
# i = 1
# while i <= 50:
#     print(fibo(i))
#     i += 1


# def fibo(num):
#     f1 = 1
#     f2 = 1
#
#     print(f1)  # 첫번째 항
#     if num >= 2:  # 두번째 항
#         print(f2)
#
#     i = 3
#     while i <= num:
#         fn = f1 + f2
#         f1 = f2
#         f2 = fn
#         print(fn)
#         i += 1
#
#
# fibo(50)


################################
# 모범 답안
prev = 0
cur = 1
i = 1

while i <= 50:
    print(cur)
    # temp = prev
    # prev = cur
    # cur = cur + temp

    prev, cur = cur, cur + prev

    i += 1
