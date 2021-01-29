# 온도 단위 바꾸기
"""
화씨 온도 -> 섭씨 온도 바꾸기

    섭씨 = ((화씨 - 32) * 5) / 9

화씨 온도를 섭씨 온도로 변환해 주는 함수
fahrenheit_to_celsius 구현
파라미터 화씨 온도 fahrenheit 받고 변환된 섭씨 온도 리턴
"""


# # 화씨 온도에서 섭씨 온도로 바꿔 주는 함수
# def fahrenheit_to_celsius(fahrenheit):
#     i = 0
#     while i < len(fahrenheit):
#         fahrenheit[i] = round((fahrenheit[i] - 32) * 5 / 9, 1)
#         i += 1

# 모범 답안
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9


temperature_list = [40, 15, 32, 64, -4, 11]
print("화씨 온도 리스트: " + str(temperature_list))  # 화씨 온도 출력

# fahrenheit_to_celsius(temperature_list)
# 모범 답안
i = 0
while i < len(temperature_list):
    temperature_list[i] = round(fahrenheit_to_celsius(temperature_list[i]), 1)
    i += 1

# 리스트의 값들을 화씨에서 섭씨로 변환하는 코드를 입력하세요.
print("섭씨 온도 리스트: " + str(temperature_list))  # 섭씨 온도 출력
