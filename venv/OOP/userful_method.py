# min, max
print(max(2, 5))  # => 5
print(max(2, 7, 5))  # => 7
print(min(2, 5))  # => 2
print(min(2, 7, 5, 11, 6))  # => 2

# sum
int_list = [1, 2, 3, 4, 5]
int_tuple = (4, 3, 6, 1, 2)
int_dict = {1: "one", 2: "two", 3: "three"}

print(sum(int_list))  # => 15
print(sum(int_tuple))  # => 16
print(sum(int_dict))  # => 6

# ternary expression
condition = True

if condition:
    condition_string = "nice"
else:
    condition_string = "not nice"
print(condition_string)  # => nice

condition_string = "nice" if condition else "not nice"
print(condition_string)  # => nice

# list comprehension
int_list = [1, 2, 3, 4, 5, 6]
squares = []

for x in int_list:
    squares.append(x ** 2)

print(squares)  # [1, 4, 9, 16, 25, 36]

squares = [x ** 2 for x in int_list]
print(squares)

# zfill method
print("1".zfill(6))
print("333".zfill(2))
print("a".zfill(8))
print("ab".zfill(8))
print("abc".zfill(8))

# ljust rjust
test1 = "12345".rjust(10, "k")
print(test1)
# 출력
# kkkkk12345

test2 = "12345".ljust(10, "k")
print(test2)
# 출력
# 12345kkkkk

from random import randint

# 1 <= N <= 20를 만족하는 랜덤한 정수(난수) N을 리턴한다.
x = randint(1, 20)
print(x)

from random import uniform

# 0 <= N <= 1을 만족하는 랜덤한 소수(난수) N을 리턴한다.
x = uniform(0, 1)
print(x)
