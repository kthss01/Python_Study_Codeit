# 짝수? 홀수?
"""
어떤 수가 짝수인지 홀수인지 판단해 주는
함수 is_evenly_divisible 구현
"""


def is_evenly_divisible(number):
    return number % 2 == 0


print(is_evenly_divisible(3))
print(is_evenly_divisible(7))
print(is_evenly_divisible(8))
print(is_evenly_divisible(218))
print(is_evenly_divisible(317))


