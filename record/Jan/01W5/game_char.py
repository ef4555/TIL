# 게임 캐릭터 생성

class character:

    def __init__(self, name):
        self.name = name
        self.hp = 100
        self.mp = 100
        self.exp = 0
    
    def create(self):
        print('캐릭터 생성')

class warrior(character):
    def __init__(self, name):
        super().__init__(name)
        self.hp = 1000

    def warrior_intro(self):
        super().create()
        print(f'나는 {self.name}이고 내 직업은 warrior')


class hunter(character):
    def __init__(self, name):
        super().__init__(name)
        self.mp = 300

    def hunter_intro(self):
        super().create()
        print(f'나는 {self.name}이고 내 직업은 hunter')     

a = warrior('kim')
b = hunter('choi')
print(b.hunter_intro())
print(b.hp)
print(b.mp)

