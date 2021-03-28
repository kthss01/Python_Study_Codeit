from math import pi, sqrt  # 원주율, 제곱근
from abc import ABC, abstractmethod


class Shape(ABC):
    """도형 클래스"""

    @abstractmethod
    def area(self) -> float:
        """도형의 넓이를 리턴한다: 자식 클래스가 오버라이딩 할 것"""
        print("도형의 넓이 계산 중!")  # ---- 추가된 코드

    @abstractmethod
    def perimeter(self) -> float:
        """도형의 둘레를 리턴한다: 자식 클래스가 오버라이딩 할 것"""

    # 일반 메소드도 사용 가능
    def larger_than(self, shape):
        """해당 인스턴스의 넓이가 파라미터 인스턴스의 넓이보다 큰지를 불린으로 나타낸다"""
        return self.area() > shape.area()

    @property
    @abstractmethod
    def x(self):
        """도형의 x 좌표 getter 메소드"""
        pass

    @property
    @abstractmethod
    def y(self):
        """도형의 y 좌표 setter 메소드"""
        pass


class EquilateralTriangle(Shape):
    """정삼각형 클래스"""

    def __init__(self, x, y, side):
        self._x = x
        self._y = y
        self.side = side

    def area(self):
        """정삼각형의 넓이를 리턴한다"""
        return sqrt(3) * self.side * self.side / 4

    def perimeter(self):
        """정삼각형의 둘레를 리턴한다"""
        return 3 * self.side

    @property
    def x(self):
        """_x getter 메소드"""
        return self._x

    @x.setter
    def x(self, value):
        """_x setter 메소드"""
        self._x = value

    @property
    def y(self):
        """_y getter 메소드"""
        return self._y

    @y.setter
    def y(self, value):
        """_y setter 메소드"""
        self._y = value


class Paint:
    """그림판 프로그램 클래스"""

    def __init__(self):
        self.shapes = []

    def add_shape(self, shape: Shape):
        """그림판에 도형을 추가한다"""
        if isinstance(shape, Shape):
            self.shapes.append(shape)
        else:
            print("넓이, 둘레를 구하는 메소드가 없는 도형은 추가할 수 없습니다.")

    def total_area_of_shapes(self):
        """그림판에 있는 모든 도형의 넓이의 합을 구한다"""
        return sum([shape.area() for shape in self.shapes])  # list comprehension

    def total_perimeter_of_shapes(self):
        """그림판에 있는 모든 도형의 둘레의 합을 구한다"""
        return sum([shape.perimeter() for shape in self.shapes])

    def __str__(self):
        """그림판에 있는 각 도형들의 정보를 출력한다"""
        res_str = "그림판 안에 있는 도형들:\n\n"
        for shape in self.shapes:
            res_str += str(shape) + "\n"
        return res_str
