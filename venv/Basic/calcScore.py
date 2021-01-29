# 학점 계산기
"""
두 시험의 점수를 합해서 최종 성적을 내는 방식
    A: 90점 이상
    B: 80점 이상 90점 미만
    C: 70점 이상 80점 미만
    D: 60점 이상 70점 미만
    F: 60점 미만

print_grade 함수 구현
    파라미터
    중간고사 점수 midterm_score와
    기말고사 점수 final_score 받고 최종 성적 출력
"""


def print_grade(midterm_score, final_score):
    total = midterm_score + final_score
    if total >= 90:
        print('A')
    elif total >= 80:
        print('B')
    elif total >= 70:
        print('C')
    elif total >= 60:
        print('D')
    else:
        print('F')


# 테스트
print_grade(40, 45)
print_grade(20, 35)
print_grade(30, 32)
print_grade(50, 45)
