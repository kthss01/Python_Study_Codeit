# 이상한 수학 문제 1
"""
while문과 if문을 활용하여,
100이하의 자연수 중 8의 배수이지만 12의 배수는 아닌 것 모두 출력
"""

i = 1
while i <= 100:
    if i % 8 == 0 and i % 12 != 0:
        print(i)
    i += 1
