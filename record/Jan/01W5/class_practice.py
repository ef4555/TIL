# 고기의 클래스를 정의하고
# 4개의 인스턴스를 만들어보자
# 마트에서 쓸만한 클래스
# 퓸종, 부위, 가격, 무게

class meat:
    category = '정육'

    def __init__(self, bread, part, price, gram):
        self.bread = bread
        self.part = part
        self.price = price
        self.gram = gram

    def sold(self, s_gram):
        print(f'{self.part}(이/가) {s_gram}만큼 팔렸습니다.')
        self.gram -= s_gram
        print(f'{self.part}(이/가) {self.gram}만큼 남았습니다.')

    def __str__(self): # __str__ 메서드는 인스턴스를 문자열처럼 사용할 수 있게 해준다.
        print('45465465')


pork_belly = meat('돼지', '삼겹살', '12000', 600)
pork_belly.sold(100)
pork_belly.sold(100)
print(pork_belly) # __str__ 메서드는 인스턴스를 문자열처럼 사용할 수 있게 해준다.

