def new_print(value_1, value_2=None, value_3=None):
    """옵셔널 파라미터"""
    if value_3 is None:
        if value_2 is None:
            print(value_1)
        else:
            print("{} {}".format(value_1, value_2))
    else:
        print("{} {} {}".format(value_1, value_2, value_3))


def print_name(first_name, last_name, email=""):
    """파라미터 이름 명시"""
    print("{}{} {}".format(last_name, first_name, email))


def print_message_and_add_numbers(message, *numbers):
    """개수가 확정되지 않은 파라미터"""
    print(message)
    return sum(numbers)


def print_message_and_add_numbers2(*numbers, message):
    """개수가 확정되지 않은 파라미터"""
    print(message)
    return sum(numbers)


new_print("this")  # 출력 : this
new_print(0.5678)  # 출력 : 0.5678
new_print("this", "that")  # 출력 : this that
new_print("this", "that", 3)  # 출력 : this that 3

print_name("태호", "성", "taheo@website.com")  # 출력 : 성태호 taeho@website.com
print_name(first_name="태호", last_name="성", email="taheo@website.com")  # 출력 : 성태호 taeho@website.com
print_name(email="taheo@website.com", first_name="태호", last_name="성")  # 출력 : 성태호 taeho@website.com
print_name(last_name="성", first_name="태호")  # 출력

print(print_message_and_add_numbers("test1", 7, 3, 5))
print(print_message_and_add_numbers("test2", 7, 3, 5, 1, 12))
print(print_message_and_add_numbers("test3", 7, 3, 5, 1))
print(print_message_and_add_numbers("test4", 7))
print(print_message_and_add_numbers("test5", 7, 2))

print(print_message_and_add_numbers2(7, 3, 5, message="test1"))
print(print_message_and_add_numbers2(7, 3, 5, 1, 12, message="test2"))
