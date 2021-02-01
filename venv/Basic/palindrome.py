# 팰린드롬
"""
토마토, 기로기
거꾸로 읽어도 똑같은 단어 팰린드롬(palindrome)

is_panlindrome 함수
팰린드롬 여부 확인
파라미터 word 팰린드롬이면 True 아니면 False 리턴
"""

def is_palindrome(word):
    # 코드를 입력하세요.
    for left in range(len(word) // 2):
        right = len(word) - left - 1
        if word[left] != word[right]:
            return False
    return True

# 테스트
print(is_palindrome("racecar"))
print(is_palindrome("stars"))
print(is_palindrome("토마토"))
print(is_palindrome("kayak"))
print(is_palindrome("hello"))