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

    def __str__(self):
        return "사용자: {}, 이메일: {}, 비밀번호: ******".format(self.name, self.email)

    @classmethod
    def number_of_users(cls):
        print("총 유저 수는 : {}입니다.".format(cls.count))

    # def number_of_users(self):
    #     print("총 유저 수는 : {}입니다.".format(self.count))


# user1 = User("Young", "young@codeit.kr", "123456")
# user2 = User("Yoonsoo", "yoonsoo@codeit.kr", "abcdef")
# user3 = User("Taeho", "taeho@codeit.kr", "123abc")
# user4 = User("Lisa", "lisa@codeit.kr", "abc123")

User.number_of_users()
# User.number_of_users(user1)
# user1.number_of_users()
