mutable_object = [1, 2, 3]
immutable_object = (1, 2, 3)

# mutable_object[0] = 4
# print(mutable_object)
#
# # immutable_object[0] = 4
# print(immutable_object)

# 불변 타입이어도 변수가 가리키는 객체는 바꿀 수 있음
tuple_x = (6, 4)
# tuple_x[0] = 4
# tuple_x[1] = 1

tuple_x = (4, 1)
tuple_x = (4, 1, 7)

print(tuple_x)
