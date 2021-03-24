class BankAccount:
    """은행 계좌 클래스"""
    interest = 0.02

    def __init__(self, owner_name, balance):
        """인스턴스 변수: name(문자열), balance(실수형)"""
        self.owner_name = owner_name
        self.balacne = balance

    def deposit(self, amount):
        """잔액 인스턴스 변수 balance를 파라미터 amount만큼 늘려주는 메소드"""
        self.balacne += amount

    def withdraw(self, amount):
        """잔액 인스턴스 변수 balance를 파라미터 amount만큼 줄여주는 메소드"""
        if self.balacne < amount:
            print("Insufficient balance!")
        else:
            self.balacne -= amount

    def add_interest(self):
        """잔액 인스턴스 변수 balance를 이자율만큼 늘려주는 메소드"""
        self.balacne *= 1 + BankAccount.interest


# help(BankAccount)
help(list)
