"""
클래스 메소드 활용
유저 인스턴스 생성에 필요한 정보가
문자열일 수도 있고 리스트 일수도 있음
각각의 형태에 대응하기 위한 클래스 메소드 구현하기
"""


class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    @classmethod
    def from_string(cls, string_params):
        parameter_list = string_params.split(",")
        name = parameter_list[0]
        email = parameter_list[1]
        password = parameter_list[2]

        return cls(name, email, password)

    @classmethod
    def from_list(cls, list_params):
        name = list_params[0]
        email = list_params[1]
        password = list_params[2]

        return cls(name, email, password)


# 유저 생성 및 초기값 설정
younghoon = User.from_string("강영훈,younghoon@codeit.kr,123456")
yoonsoo = User.from_list(["이윤수", "yoonsoo@codeit.kr", "abcdef"])

print(younghoon.name, younghoon.email, younghoon.password)
print(yoonsoo.name, yoonsoo.email, yoonsoo.password)
