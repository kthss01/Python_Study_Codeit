def print_hello():
    print("안녕하세요!")


# 데코레이터 함수
def add_print_to(original):
    def wrapper():
        print("함수 시작")
        original()
        print("함수 끝")
    return wrapper


# add_print_to(print_hello)()

print_hello = add_print_to(print_hello)
print_hello()
