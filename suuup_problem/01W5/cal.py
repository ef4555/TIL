import random 

class ClassHelper:

    def __init__(self, namelist):
        self.namelist = namelist

    def pick(self, n):
        return random.sample(self.namelist, n)

    def match_pair(self):
        a_list = []
        while len(self.namelist) > 3:
            a = random.sample(self.namelist, 2)
            a_list.append(a)
            for i in a:
                self.namelist.remove(i)
        a_list.append(self.namelist)
        return a_list
        




ch = ClassHelper(['김해피', '이해킹', '조민지', '박영수', '정민수', '최예훈', '김동욱'])

print(ch.pick(1))
print(ch.pick(1))
print(ch.pick(2))
print(ch.pick(3))
print(ch.pick(4))

print(ch.match_pair())
