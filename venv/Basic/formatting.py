num_1 = 1
num_2 = 3
print("{0} 나누기 {1}은 {2:.4f}입니다.".format(num_1, num_2, num_1/num_2))

# 가장 오래된 방식 %
name = "김태훈"
age = 31
print("제 이름은 %s이고 %d살입니다." % (name, age))

# 현재 가장 많이 쓰는 방식 (format 메소드)
print("제 이름은 {}이고 {}살입니다.".format(name, age))

# 새로운 방식 (f-string)
print(f"제 이름은 {name}이고 {age}살입니다.")
"""
파이썬 버전 3.6부터 새롭게 나온 방식
"""