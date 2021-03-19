class User:
    count = 0

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

        User.count += 1

    def say_hello(self):
        # 인사 메세지 출력 메소드
        print("안녕하세요! 저는 {}입니다.".format(self.name))


user1 = User("Young", "young@codeit.kr", "123456")

print(type(user1))

print(type(2))
print(type("string"))
print(type([]))
print(type({}))
print(type(()))


def print_hello():
    print("hi")


print(type(print_hello))

int_list = []

int_list.append(1)
int_list.append(3)
int_list.append(7)

print(int_list)
