# 모듈 사용해 보기
"""
이미지를 다루는 모듈을 만들고 사용해보기

이미지는 비트맵 형식으로 표현
비트맵은 각 픽셀(이미지를 구성하는 가장 작은 점들)의 색깔을 이진수로 저장해 놓은 맵(지도)
이번 과제는 흑백 이미지만 다뤄볼 것
참고로 비트(bit) 0 또는 1의 값을 뜻함

중첩된 리스트로 사용

cil 모듈
cil은 Codeit Imaging Library의 약자
cli.py 파일 안에
이미지를 읽어오고, 저장하고, 디스플레이하는데 쓰이는 유틸리티 함수들이 몇 개 있음
read_image(filepath), save_image(img, filepath)
    비트맵 이미지 파일을 읽어와서 중첩된 리스트로 만들어 주고
    중첩된 리스트를 비트맵 형식으로 저장해주는 함수
display(img) 함수
    이미지 출력

과제
cil.py 에 있는 invert(img) 함수 구현
주어진 이미지의 색상을 반전시켜 새로운 이미지 리턴
원본 이미지는 바뀌면 안됨

invert 함수 구현을 위해 다른 함수를 만들어둠

empty_image(height, width) 함수
    높이가 height, 너비가 width인 '비어있는 이미지'(중첩 리스트)를 만들어줌
    리스트의 값은 모두 -1로 채워짐

invert_bit(bit) 함수
    비트를 반전해줌줌
"""

# cil 모듈을 임포트해 주세요
### 코드를 작성해 주세요 ###
import cil
# cil 모듈의 display 함수를 직접 임포트해 주세요
### 코드를 작성해 주세요 ###
from cil import display

img1 = cil.read_image('img1.txt')
img2 = cil.read_image('img2.txt')

inverted_img1 = cil.invert(img1)
inverted_img2 = cil.invert(img2)

print('원본 이미지')
print('\nimage1:')
display(img1)
print('\nimage2:')
display(img2)

print('\n색상 반전된 이미지')
print('\nimage1:')
display(inverted_img1)
print('\nimage2:')
display(inverted_img2)

# 채점 코드
print()
print('cil' in dir())
print('display' in dir())