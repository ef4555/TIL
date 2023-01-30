# 고기의 클래스를 정의하고
# 4개의 인스턴스를 만들어보자
# 마트에서 쓸만한 클래스
# 퓸종, 부위, 가격, 무게

class Doggy:

    birth_of_dogs = 0
    num_of_dogs = 0

    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
        Doggy.birth_of_dogs += 1
        Doggy.num_of_dogs += 1

    def bark(self):
        print(f'{self.name} 멍멍')

    def get_status(self):
        print(f'{Doggy.num_of_dogs}')
        print(f'{Doggy.birth_of_dogs}')

d1 = Doggy('a', '11')
d2 = Doggy('b', '12')
d3 = Doggy('c', '1123123')
d1.bark()
d2.bark()

d1.get_status()
