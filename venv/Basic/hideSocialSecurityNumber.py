# 주민등록번호 가리기
"""
주민등록번호 YYMMDD-abcdefg는 총 13자리
YYMMDD 생년월일 의미
a - 성별
bc - 출생등록지에 해당하는 지방자치단체의 고유번호
defg - 임의의 번호

마지막 네자리 가려주려고 함
mask_security_number 함수
파라미터 문자열 security_number
security_number의 마지막 네 글자 '*'로 대체한 새 문자열로 리턴
security_number에는 작대기 기호(-)가 포함될 수도 있고 안될수도 있음
상관없이 마지막 네글자 대체하기
"""

def mask_security_number(security_number):
    # 코드를 입력하세요.
    return security_number[:-4] + "****"

# 테스트
print(mask_security_number("880720-1234567"))
print(mask_security_number("8807201234567"))
print(mask_security_number("930124-7654321"))
print(mask_security_number("9301247654321"))
print(mask_security_number("761214-2357111"))
print(mask_security_number("7612142357111"))