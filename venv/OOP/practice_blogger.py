"""
블로그 유저 만들기
    BlogUser 클래스
        인스턴스 변수 (타입)
            name(문자열) : 블로그 사용자의 이름
            posts(리스트) : 블로그 게시글들 담을 리스트

        메소드
            __init__ : 인스턴스 변수가 설정되는 메소드
            add_post : 블로그 사용자의 블로그 게시글 리스트에 새로운 게시글 추가
            show_all_posts : 블로그 사용자가 올린 모든 게시글 출력
            __str__ : 블로그 사용장의 간단한 인사외 이름 리턴
"""


class Post:
    # 게시글 클래스
    def __init__(self, date, content):
        # 게시글은 속성으로 작성 날짜와 내용을 갖는다
        self.date = date
        self.content = content

    def __str__(self):
        # 게시글의 정보를 문자열로 리턴하는 메소드
        return "작성 날짜: {}\n내용: {}".format(self.date, self.content)


class BlogUser:
    # 블로그 유저 클래스
    def __init__(self, name):
        """
        블로그 유저는 속성으로 이름, 게시글들을 갖는다
        posts는 빈 배열로 초기화한다
        """
        self.name = name
        self.posts = []

    def add_post(self, date, content):
        # 새로운 게시글 추가
        self.posts.append(Post(date, content))

    def show_all_posts(self):
        # 블로그 유저의 모든 게시글 출력
        for post in self.posts:
            print(post)

    def __str__(self):
        # 간단한 인사와 이름을 문자열로 리턴
        return f"안녕하세요 {self.name}입니다.\n"


# 블로그 유저 인스턴스 생성
blog_user_1 = BlogUser("성태호")

# 블로그 유저 인스턴스 출력(인사, 이름)
print(blog_user_1)

# 블로그 유저 게시글 2개 추가
blog_user_1.add_post("2019년 8월 30일", """
오늘은 내 생일이였다.
많은 사람들이 축하해줬다.
행복했다.
""")

blog_user_1.add_post("2019년 8월 31일", """
재밌는 코딩 교육 사이트를 찾았다.
코드잇이란 곳인데 최고다.
같이 공부하실 분들은 www.codeit.kr로 오세요!
""")

# 블로그 유저의 모든 게시글 출력
blog_user_1.show_all_posts()
