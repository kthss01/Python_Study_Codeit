"""
속성이 없는 계산기
계산기 클래스 만들기
    변수 없는 클래스에서는 정적 메소드 정의
    SimpleCalculator 정적 메소드 완성
        add : 파라미터로 받은 두 숫자의 합 리턴
        subtract : 파라미터로 받은 두 숫자의 차 리턴
        multiply : 파라미터로 받은 두 숫자의 곱 리턴
        divide : 파라미터로 받은 두 숫자의 나누기 리턴
"""


class SimpleCalculator:
    # 계산기 클래스
    @staticmethod
    def add(first_number, second_number):
        return first_number + second_number

    @staticmethod
    def subtract(first_number, second_number):
        return first_number - second_number

    @staticmethod
    def multiply(first_number, second_number):
        return first_number * second_number

    @staticmethod
    def divide(first_number, second_number):
        return first_number / second_number


# 계산기 인스턴스 생성
calculator = SimpleCalculator()

# 계산기 연산 호출
print(calculator.add(4, 5))
print(calculator.subtract(4, 5))
print(calculator.multiply(4, 5))
print(calculator.divide(4, 5))
