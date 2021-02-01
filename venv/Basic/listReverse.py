# 리스트 뒤집기
"""
리스트 원소들의 순서 뒤집기
numbers 리스트 for문을 사용하여 거꾸로 뒤집기
"""

numbers = [2, 3, 5, 7, 11, 13, 17, 19]

# 리스트 뒤집기
# 코드를 입력하세요.

length = len(numbers)
# for x in range(int(length / 2)):
for x in range(length // 2):
    y = length - x - 1
    # temp = numbers[x]
    # numbers[x] = numbers[y]
    # numbers[y] = temp

    # ,로만 각 요소 구분해도 튜플로 인식됨됨
   numbers[x], numbers[y] = numbers[y], numbers[x]

print("뒤집어진 리스트: " + str(numbers))