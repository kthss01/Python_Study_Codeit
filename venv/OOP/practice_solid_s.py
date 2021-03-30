"""
모든 것을 아는 학생

Student 클래스
    학생 기본 정보 수정
    학점 추가
    평균 학점 계산
    성적표 출력

God object -> 단일 책임 원칙에 맞게 바꾸기
"""


# class Student:
#     def __init__(self, name, id, major):
#         self.info = StudentInfo(name, id, major)
#         self.grades = Grade()
#
#     def __str__(self):
#         """학생 성적표 출력 메소드"""
#         return "코드잇 대학 성적표\n\n" + str(self.info) \
#                + "\n평균 학점:{}".format(self.grades.get_average_gpa())
#
#
# class StudentInfo:
#     """학생 정보 클래스"""
#
#     def __init__(self, name, id, major):
#         self.name = name
#         self.id = id
#         self.major = major
#
#     def change_student(self, new_name, new_id, new_major):
#         """학생 기본 정보 수정 메소드"""
#         self.name = new_name
#         self.id = new_id
#         self.major = new_major
#
#     def __str__(self):
#         """학생 정보 출력 메소드"""
#         return "학생 이름:{}\n학생 번호:{}\n소속 학과:{}".format(self.name, self.id, self.major)
#
#
# class Grade:
#     """학점 클래스"""
#
#     def __init__(self):
#         self.grades = []
#
#     def add_grade(self, grade):
#         """학점 추가 메소드"""
#         if 0 <= grade <= 4.3:
#             self.grades.append(grade)
#         else:
#             print("수업 학점은 0과 4.3 사이여야 합니다!")
#
#     def get_average_gpa(self):
#         """평균 학점 계산 메소드"""
#         return sum(self.grades) / len(self.grades)
#
#
# # 학생 인스턴스 정의
# younghoon = Student("강영훈", 20120034, "통계학과")
# younghoon.info.change_student("강영훈", 20130024, "컴퓨터 공학과")
#
# # 학생 성적 추가
# younghoon.grades.add_grade(3.0)
# younghoon.grades.add_grade(3.33)
# younghoon.grades.add_grade(3.67)
# younghoon.grades.add_grade(4.3)
#
# # 학생 성적표
# print(younghoon)


""" 풀이 """


class StudentProfile:
    """학생 기본 정보 클래스"""

    def __init__(self, name, id, major):
        self.name = name
        self.id = id
        self.major = major

    def change_info(self, new_name, new_id, new_major):
        """학생 기본 정보 수정 메소드"""
        self.name = new_name
        self.id = new_id
        self.major = new_major


class GPAManager:
    """학생 학점 관리 클래스"""

    def __init__(self, grades):
        self.grades = grades

    def add_grade(self, grade):
        """학점 추가 메소드"""
        if 0 <= grade <= 4.3:
            self.grades.append(grade)
        else:
            print("수업 학점은 0과 4.3 사이여야 합니다!")

    def get_average_gpa(self):
        """평균 학점 계산"""
        return sum(self.grades) / len(self.grades)


class ReportCardPrinter:
    """성적표 출력 클래스"""

    def __init__(self, student_profile, gpa_manager):
        self.student_profile = student_profile
        self.gpa_manager = gpa_manager

    def print(self):
        """학생 성적표 출력 메소드"""
        print("코드잇 대학 성적표\n\n학생 이름:{}\n학생 번호:{}\n소속 학과:{}\n평균 학점:{}" \
              .format(self.student_profile.name, self.student_profile.id, \
                      self.student_profile.major, self.gpa_manager.get_average_gpa()))


class Student:
    """코드잇 대학생을 나타내는 클래스"""

    def __init__(self, name, id, class_year):
        self.profile = StudentProfile(name, id, class_year)
        self.grades = []
        self.gpa_manager = GPAManager(self.grades)
        self.report_card_printer = ReportCardPrinter(self.profile, self.gpa_manager)


# 학생 인스턴스 정의
younghoon = Student("강영훈", 20120034, "통계학과")
younghoon.profile.change_info("강영훈", 20130024, "컴퓨터 공학과")

# 학생 성적 추가
younghoon.gpa_manager.add_grade(3.0)
younghoon.gpa_manager.add_grade(3.33)
younghoon.gpa_manager.add_grade(3.67)
younghoon.gpa_manager.add_grade(4.3)

# 학생 성적표
younghoon.report_card_printer.print()


""" 문제 """
# class Student:
#     def __init__(self, name, id, major):
#         self.name = name
#         self.id = id
#         self.major = major
#         self.grades = []
#
#     def change_student_info(self, new_name, new_id, new_major):
#         """학생 기본 정보 수정 메소드"""
#         self.name = new_name
#         self.id = new_id
#         self.major = new_major
#
#     def add_grade(self, grade):
#         """학점 추가 메소드"""
#         if 0 <= grade <= 4.3:
#             self.grades.append(grade)
#         else:
#             print("수업 학점은 0과 4.3 사이여야 합니다!")
#
#     def get_average_gpa(self):
#         """평균 학점 계산 메소드"""
#         return sum(self.grades) / len(self.grades)
#
#     def print_report_card(self):
#         """학생 성적표 출력 메소드"""
#         print("코드잇 대학 성적표\n\n학생 이름:{}\n학생 번호:{}\n소속 학과:{}\n평균 학점:{}" \
#               .format(self.name, self.id, self.major, self.get_average_gpa()))
#
#
# # 학생 인스턴스 정의
# younghoon = Student("강영훈", 20120034, "통계학과")
# younghoon.change_student_info("강영훈", 20130024, "컴퓨터 공학과")
#
# # 학생 성적 추가
# younghoon.add_grade(3.0)
# younghoon.add_grade(3.33)
# younghoon.add_grade(3.67)
# younghoon.add_grade(4.3)
#
# # 학생 성적표
# younghoon.print_report_card()
