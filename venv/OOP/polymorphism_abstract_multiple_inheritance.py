from abc import ABC, abstractmethod


class Message(ABC):
    @abstractmethod
    def print_message(self) -> None:
        pass

    def __str__(self):  # ----- 중복되는 일반 메소드
        return "Message 클래스의 인스턴스"


class Sendable(ABC):
    @abstractmethod
    def send(self, destination: str) -> None:
        pass

    def __str__(self):  # ----- 중복되는 일반 메소드
        return "Sendable 클래스의 인스턴스"


class Email(Message, Sendable):
    def __init__(self, content, user_email):
        self.content = content
        self.user_email = user_email

    def print_message(self):
        print("이메일 내용입니다:\n{}".format(self.content))

    def send(self, destination):
        print("이메일을 주소 {}에서 {}로 보냅니다!".format(self.user_email, destination))
