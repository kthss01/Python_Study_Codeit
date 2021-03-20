"""
게임 캐릭터 만들기
    GameCharacter 클래스
        인스턴스 변수 (타입)
            name(문자열) : 캐릭터의 이름
            hp(숫자형) : 캐릭터의 체력
            power(숫자형) : 캐릭터의 공격
        인스턴스 메소드
            __init__ : 사용할 모든 인스턴스 변수 설정
            is_alive : 게임 캐릭터의 체력이 0보다 큰지 확인
                0 초과면 True 아니면 False
            get_attacked : 게임 캐릭터의 체력이 0보다 큰 상태라면
                파라미터로 받은 공격력만큼 체력을 깎는다
                조건
                is_alive 메소드를 사용해서 인스턴스가 살아있을 때만 체력을 깍음
                    이미 캐릭터가 죽어있으면 죽었다는 메세지 출력
                남은 체력보다 공격력이 더 크면 체력(hp) 0으로 설정
            attack : 파라미터로 받은 다른 캐릭터의 체력을 자신의 공격력만큼 깍는다
                조건
                is_alive 메소드를 이용해서 살아있는 인스턴스만 공격을 할 수 있도록 함
                get_attacked 메소드 사용
            __str__ : 게임 캐릭터의 의미있는 정보를 포함한 문자열 리턴
"""


class GameCharacter:
    # 게임 캐릭터 클래스
    def __init__(self, name, hp, power):
        # 게임 캐릭터는 속성으로 이름, hp, 공격력을 갖는다
        self.name = name
        self.hp = hp
        self.power = power

    def is_alive(self):
        # 게임 캐릭터가 살아있는지(체력이 0이 넘는지) 확인하는 메소드
        return self.hp > 0

    def get_attacked(self, damage):
        """
        게임 캐릭터가 살아있으면 공격한 캐릭터의 공격력만큼 체력을 깎는 메소드
        조건:
            1. 이미 캐릭터가 죽었으면 죽었다는 메시지를 출력한다
            2. 남은 체력보다 공격력이 더 크면 체력은 0이 된다.
        """
        if self.is_alive():
            self.hp = self.hp - damage if self.hp >= damage else 0
        else:
            print("{}님은 이미 죽었습니다.".format(self.name))

    def attack(self, other_character):
        # 게임 캐릭터가 살아있으면 파라미터로 받은 다른 캐릭터의 체력을 자신의 공격력만큼 깎는다.
        if self.is_alive():
            other_character.get_attacked(self.power)

    def __str__(self):
        # 게임 캐릭터의 의미있는 정보를 포함한 문자열을 리턴한다.
        return "{}님의 hp는 {}만큼 남았습니다.".format(self.name, self.hp)


# 게임 캐릭터 인스턴스 생성
character_1 = GameCharacter("Ww영훈전사wW", 200, 30)
character_2 = GameCharacter("Xx지웅최고xX", 100, 50)

# 게임 캐릭터 인스턴스들 서로 공격
character_1.attack(character_2)
character_2.attack(character_1)
character_2.attack(character_1)
character_2.attack(character_1)
character_2.attack(character_1)
character_2.attack(character_1)

# 게임 캐릭터 인스턴스 출력
print(character_1)
print(character_2)
