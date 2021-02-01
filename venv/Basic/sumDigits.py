# 자릿수 합 구하기
"""
함수 sum_digit
파라미터 정수형 num num의 각 자릿수를 더한 값 리턴

sum_digit 함수 작성
sum_digit(1)부터 sum_digit(1000)까지의 합 구해서 출력
"""


# 자리수 합 리턴
def sum_digit(num):
    # 코드를 입력하세요.
    # sum = 0
    #
    # while num != 0:
    #     sum += num % 10
    #     num //= 10
    #
    # return sum
    total = 0
    str_num = str(num)

    for digit in str_num:
        total += int(digit)

    return total

# sum_digit(1)부터 sum_digit(1000)까지의 합 구하기
# 코드를 입력하세요.
digit_total = 0

for i in range(1, 1001):
    digit_total += sum_digit(i)

print(digit_total)