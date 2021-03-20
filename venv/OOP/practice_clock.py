"""
혹시... 시간이 어떻게 되나요

    시계 만들기
        1. 현재 시간 설정
        2. 현재 시간 변경
        3. 현재 시간에 1초씩 더하기
"""


class Clock:
    def __init__(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second

    def set(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second

    def tick(self):
        self.second = self.second + 1
        if self.second >= 60:
            self.second -= 60
            self.minute += 1
            if self.minute >= 60:
                self.minute -= 60
                self.hour += 1
                if self.hour >= 24:
                    self.hour -= 24

    def __str__(self):
        # return f"{self.hour:02d}:{self.minute:02d}:{self.second:02d}"
        # return "{:02d}:{:02d}:{:02d}".format(self.hour, self.minute, self.second)
        # return "{0:02d}:{1:02d}:{2:02d}".format(self.hour, self.minute, self.second)
        hour = str(self.hour).zfill(2)
        minute = str(self.minute).zfill(2)
        second = str(self.second).zfill(2)
        return f"{hour}:{minute}:{second}"


# 1시 30분 48초인 시계 인스턴스 생성
clock = Clock(1, 30, 48)

# 13초를 늘린다
for i in range(13):
    clock.tick()

# 시계의 현재 시간 출력
print(clock)

# 2시 3분 58초로 시계 세팅
clock.set(2, 3, 58)

# 5초를 늘린다
for i in range(5):
    clock.tick()

# 시계의 현재 시간 출력
print(clock)

# 23시 59분 57초로 세팅
clock.set(23, 59, 57)

# 5초를 늘린다
for i in range(5):
    clock.tick()

# 시계의 현재 시간 출력
print(clock)
