# import math
#
# math.log10()
# maht.cos()

# from math import log10, cos
#
# log10()
# cos()

import os
"파이썬으로 운영체제를 조작하거나 운영체제에 대한 정보를 가져올 수 있음"

# 현재 어떤 계정으로 로그인 돼있는지 확인
print(os.getlogin())

# 현재 파일의 디렉토리 확인
print(os.getcwd())

# 현재 프로세스 ID 확인
print(os.getpid())

print()

import os.path
"파일 경로를 다룰 때 쓰임"

# 프로젝트 디렉토리 경로 '/Users/codeit/PycharmProjects/standard_modules'
# 현재 파일 경로 '/Users/codeit/PycharmProjects/standard_modules/main.py'

# 주어진 경로를 절대 경로로
print(os.path.abspath('..'))

# 주어진 경로를 현재 디렉토리를 기준으로 한 상대 경로로
print(os.path.relpath('/Users/codeit/PycharmProjects'))

# 주어진 경로들을 병합
print(os.path.join('/Users/codeit/PycharmProjects', 'standard_modules'))

print()

import re
"특정한 규칙/패턴을 가진 문자열을 표현하는데 사용"

# 알파벳으로 구성된 단어들만 매칭
pattern = re.compile('^[A-Za-z]+$')
print(pattern.match('I'))
print(pattern.match('love'))
print(pattern.match('python3'))

print()

# 숫자가 포함된 단어들만 매칭
pattern = re.compile('.*\d+')
print(pattern.match('I'))
print(pattern.match('love'))
print(pattern.match('python3'))

print()

import pickle
"파이썬 오브젝트(객체)를 바이트(byte) 형식으로 바꿔서 파일에 저장할 수 있고" \
"저장된 오브젝트를 읽어올 수도 있음"

# 딕셔너리 오브젝트
obj = {'my' : 'dictionary'}

# obj를 filename.pickle 파일에 저장
with open('filename.pickle', 'wb') as f:
    pickle.dump(obj, f)

# filename.pickle에 있는 오브젝트를 읽어옴
with open('filename.pickle', 'rb') as f:
    obj = pickle.load(f)

print(obj)

print()

import json
"pickle과 비슷하지만 오브젝트를 json 형식으로 바꿔줌" \
"json 형식에 맞는 데이터 (기본 데이터 타입들, 리스트, 딕셔너리)만 바꿀 수 있음"

# 딕셔너리 오브젝트
obj = {'my' : 'dictionary'}

# obj를 filename.json 파일에 저장
with open('filename.json', 'w') as f:
    json.dump(obj, f)

# filename.json에 있는 오브젝트를 읽어옴
with open('filename.json', 'r') as f:
    obj = json.load(f)

print(obj)

print()

import copy
"파이썬 오브젝트를 복사할 때 쓰임"

# '=' 연산자는 실제로 리스트 복사 안함
# 리스트를 복사하려면 슬라이싱을 사용하거나 copy.copy() 함수를 사용해야 함
a = [1, 2, 3]
b = a
c = a[:]
d = copy.copy(a)
a[0] = 4
print(a, b, c, d)

# 하지만 오브젝트 안에 오브젝트가 있는 경우 copy.copy() 함수는
# 가장 바깥에 있는 오브젝트만 복사함
# 오브젝트를 재귀적으로 복사하려면 copy.deepcopy() 함수를 사용해야함
a = [[1,2,3], [4,5,6], [7,8,9]]
b = copy.copy(a)
c = copy.deepcopy(a)
a[0][0] = 4
print(a, b, c)

import sqlite3
"파이썬에서 SQLite 데이터베이스를 사용할 수 있음"

# # 데이터베이스 연결
# conn = sqlite3.connect('example.db')
#
# # SQL 문 실행
# c = conn.cursor()
# c.execute('''SELECT ... FROM ... WHERE ... ''')
#
# # 가져온 데이터를 파이썬에서 사용
# rows = c.fetchall()
# for row in rows:
#     print(row)