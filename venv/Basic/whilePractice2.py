# while문 연습 2
"""
while문을 사용하여,
100 이상의 자연수 중 가장 작은 23의 배수 출력
"""

i = 100
# while True:
#     if i % 23 == 0:
#         print(i)
#         break
#     i += 1

while i % 23 != 0:
    i += 1

print(i)