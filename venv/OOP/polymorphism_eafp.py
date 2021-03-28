from math import pi, sqrt  # 원주율, 제곱근


class Shape:
    """도형 클래스"""

    def area(self) -> float:
        """도형의 넓이를 리턴한다: 자식 클래스가 오버라이딩 할 것"""
        pass

    def perimeter(self) -> float:
        """도형의 둘레를 리턴한다: 자식 클래스가 오버라이딩 할 것"""
        pass


class Rectangle(Shape):
    """직사각형 클래스"""

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        """직사각형의 넓이를 리턴한다"""
        return self.width * self.height

    def perimeter(self):
        """직사각형의 둘레를 리턴한다"""
        return 2 * self.width + 2 * self.height

    def __str__(self):
        """직사각형의 정볼르 문자열로 리턴한다"""
        return "밑변 {}, 높이 {}인 직사각형".format(self.width, self.height)


class Circle(Shape):
    """원 클래스"""

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        """원의 넓이를 리턴한다"""
        return pi * self.radius * self.radius

    def perimeter(self):
        """원의 둘레를 리턴한다"""
        return 2 * pi * self.radius

    def __str__(self):
        """원의 정보를 문자열로 리턴한다"""
        return "반지름 {}인 원".format(self.radius)


class Cylinder:
    """원통 클래스"""

    def __init__(self, radius, height):
        self.radius = radius
        self.height = height

    def __str__(self):
        """원통의 정보를 문자열로 리턴한다"""
        return "밑면 반지름 {}, 높이 {}인 원기둥".format(self.radius, self.height)


class EquilateralTriangle(Shape):
    """정삼각형 클래스"""

    def __init__(self, side):
        self.side = side

    def area(self):
        """정삼각형의 넓이를 리턴한다"""
        return sqrt(3) * self.side * self.side / 4

    def perimeter(self):
        """정삼각형의 둘레를 리턴한다"""
        return 3 * self.side


class Paint:
    """그림판 프로그램 클래스"""

    def __init__(self):
        self.shapes = []

    def add_shape(self, shape: Shape):
        """그림판에 도형 인스턴스 shape를 추가한다. 단, shape은 추상 클래스 Shape의 인스턴스여야 한다."""
        self.shapes.append(shape)

    def total_area_of_shapes(self):
        """그림판에 있는 모든 도형의 넓이의 합을 구한다"""

        total_area = 0

        for shape in self.shapes:
            try:
                total_area += shape.area()
            except (AttributeError, TypeError):
                print("그림판에 area 메소드가 없거나 잘못 정의되어 있는 인스턴스 {}가 있습니다.".format(shape))

        return total_area

    def total_perimeter_of_shapes(self):
        """그림판에 있는 모든 도형의 둘레의 합을 구한다"""

        total_perimeter = 0

        for shape in self.shapes:
            try:
                total_perimeter += shape.perimeter()
            except (AttributeError, TypeError):
                print("그림판에 perimeter 메소드가 없거나 잘못 정의되어 있는 인스턴스 {}가 있습니다.".format(shape))

        return total_perimeter

    def __str__(self):
        """그림판에 있는 각 도형들의 정보를 출력한다"""
        res_str = "그림판 안에 있는 도형들:\n\n"
        for shape in self.shapes:
            res_str += str(shape) + "\n"
        return res_str
