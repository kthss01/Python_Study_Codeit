from shapes import PI

print('area 모듈 이름: {}'.format(__name__))

# PI = 3.14


def circle(radius):
    return PI * radius * radius


def square(length):
    return length * length


if __name__ == '__main__':
    print(5 == circle(5))

# __name__
# __main__