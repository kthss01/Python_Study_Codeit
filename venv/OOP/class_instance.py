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

    def login(self, my_email, my_password):
        # 로그인 메소드
        if (self.email == my_email) and (self.password == my_password):
            print("로그인 성공, 환영합니다.")
        else:
            print("로그인 실패, 없는 아이디이거나 잘못된 비밀번호입니다.")

    def check_name(self, name):
        # 파라미터로 받는 name이 유저의 이름과 같은지 불린으로 리턴하는 메소드
        return self.name == name

    def __str__(self):
        return "사용자: {}, 이메일: {}, 비밀번호: ******".format(self.name, self.email)


# user1 = User()
# user2 = User()
# user3 = User()

# user1.name = "김대위"
# user1.email = "captain@codeit.kr"
# user1.password = "12345"
#
# user2.name = "강영훈"
# user2.email = "younghoon@codeit.kr"
# user2.password = "98765"
#
# user3.name = "최지웅"
# user3.email = "jiwoong@codeit.kr"
# user3.password = "78945"

user1 = User("Young", "young@codeit.kr", "123456")
user2 = User("Yoonsoo", "yoonsoo@codeit.kr", "abcdef")
user3 = User("Taeho", "taeho@codeit.kr", "123abc")
user4 = User("Lisa", "lisa@codeit.kr", "abc123")

# print(user1.email)
# print(user2.password)

# print(user1.age)

# User.say_hello(user1)
# User.say_hello(user2)
# user1.say_hello()

# user1.login("captain@codeit.kr", "12345")

# print(user1.check_name("김대위"))
# print(user1.check_name("강영훈"))

# print(user1)
# print(user2)

# User.count = 1
# user1.count = 5

print(User.count)
print(user1.count)

