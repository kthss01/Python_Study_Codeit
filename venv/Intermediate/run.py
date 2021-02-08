print('run 모듈 이름: {}'.format(__name__))
#
# import area
#
# print(area.circle(2))
# print(area.square(3))
# print(area.PI)

# from area import circle, square
# print(circle(2))
# print(square(3))

# import area as ar
# print(ar.circle(2))

# from area import square as sq
# print(sq(3))
#
# from area import *
# print(square(3))
# print(circle(2))

# print(dir(area))
# print(dir())
# import area


# from area import circle, square as sq
# import area
#
# def square(length):
#     return 4 * length
#
# print(dir())
# # print(sq(3))
# print(area.square(3))
# print(square(3))
#
# import sys
#
# print(sys.path)
#
# sys.path.append('C:\\Users\\codeit\\Desktop')  # Windows

print('run 파일 실행됨')

# # import shapes.volume
# import shapes.volume as vol
#
# # print(shapes.volume.cube(3))
# print(vol.cube(3))
#
# from shapes.area import square
#
# print(square(3))
#
# from shapes import volume
#
# import shapes.volume  # 위 코드는 이 코드와 같음

import shapes

print(shapes.area.circle(2))  # __init__ 을 써줘야 함 그냥하면 안됨