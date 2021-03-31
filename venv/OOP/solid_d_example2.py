from abc import ABC, abstractmethod


class IWeapon(ABC):
    """무기 클래스"""

    @abstractmethod
    def use_on(self, other_character):
        pass


# 하위 모듈
class Sword(IWeapon):
    """검 클래스"""

    def __init__(self, damage):
        self.damage = damage

    def use_on(self, other_character):
        """검 사용 메소드"""
        other_character.get_damage(self.damage)


class Gun(IWeapon):
    """총 클래스"""

    def __init__(self, damage, num_rounds):
        self.damage = damage
        self.num_rounds = num_rounds  # 총알 갯수

    def use_on(self, other_character):
        """총 사용 메소드"""
        if self.num_rounds > 0:
            other_character.get_damage(self.damage)
            self.num_rounds -= 1
        else:
            print("총알이 없어 공격할 수 없습니다다")


# 상위 모듈
class GameCharacter:
    """게임 캐릭터 클래스"""

    def __init__(self, name, hp, weapon: IWeapon):
        self.name = name
        self.hp = hp
        self.weapon = weapon

    def attack(self, other_character):
        """다른 유저를 공격하는 메소드"""
        if self.hp > 0:
            self.weapon.use_on(other_character)  # 이 부분에서 하위 모듈에 의존
        else:
            print(self.name + "님은 사망해서 공격할 수 없습니다.")

    def change_weapon(self, new_weapon):
        """무기를 바꾸는 메소드"""
        self.weapon = new_weapon

    def get_damage(self, damage):
        """캐릭터가 공격받았을 때 자신의 체력을 깎는 메소드"""
        if self.hp <= damage:
            self.hp = 0
            print(self.name + "님은 사망했습니다.")
        else:
            self.hp -= damage

    def __str__(self):
        """남은 체력을 문자열로 리턴하는 메소드"""
        return self.name + "님은 hp: {}이(가) 남았습니다.".format(self.hp)


# 무기 인스턴스들 정의
bad_sword = Sword(1)
gun = Gun(100, 10)

# 게임 캐릭터 인스턴스 정의
game_character_1 = GameCharacter("홍길동", 100, bad_sword)
game_character_2 = GameCharacter("아무개", 1000, gun)

# 캐릭터들이 서로 공격
game_character_1.attack(game_character_2)
game_character_1.attack(game_character_2)
game_character_1.attack(game_character_2)
game_character_2.attack(game_character_1)

# 캐릭터 출력
print(game_character_1)
print(game_character_2)
