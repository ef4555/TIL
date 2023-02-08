
class Doggy:
    num_of_dogs = 0
    birth_of_dogs = 0


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
    
    def die(self):
        print('사망')
        Doggy.num_of_dogs -= 1

d1 = Doggy('aaa','진도')
d2 = Doggy('aaaasd','시바')
d1.die()
d2.get_status()



# d1.get_status()
# del d1
# d2.get_status()

