# 리스트 함수 활용하기
"""
numbers라는 리스트 만들고 리스트 출력
append 이용해서 numbers에 1,7,3,6,5,2,13,14 순서대로 추가 후 리스트 출력
numbers 리스트의 원소들 중 홀수는 모두 제거 그 후 다시 리스트 출력
numbers 리스트의 인덱스 0자리에 20이라는 수 삽입 후 출력
numbers 리스트 정렬 후 출력
"""

# 빈 리스트 만들기
numbers = []
print(numbers)

# numbers에 값들 추가
# 코드를 입력하세요
numbers += [1, 7, 3, 6, 5, 2, 13, 15]
# numbers.extend([1, 7, 3, 6, 5, 2, 13, 14])
print(numbers)

# numbers에서 홀수 제거
# 코드를 입력하세요
i = 0
while i < len(numbers):
    if numbers[i] % 2 != 0:
        del numbers[i]
    else:
        i += 1

# i=len(numbers)-1
# while i>=0:
#     if numbers[i]%2 != 0:
#         del numbers[i]
#     i-=1

print(numbers)

# numbers의 인덱스 0 자리에 20이라는 값 삽입
# 코드를 입력하세요
numbers.insert(0, 20)
print(numbers)

# numbers를 정렬해서 출력
# 코드를 입력하세요
numbers.sort()
print(numbers)
