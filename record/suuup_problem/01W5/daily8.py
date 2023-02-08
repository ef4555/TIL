class Point:
    def __init__(self, x, y):
        self.x = (x, y)



class Rectangle:
    def __init__(self, aaa, bbb):
        self.p1 = aaa
        self.p2 = bbb


    def get_area(self):
        return (self.p2.x[0]-self.p1.x[0])*(self.p1.x[1]-self.p2.x[1])
        
    def get_perimeter(self):
        return (self.p2.x[0]-self.p1.x[0])*2 + (self.p1.x[1]-self.p2.x[1])*2

    def is_square(self):
        if (self.p2.x[0]-self.p1.x[0]) == (self.p1.x[1]-self.p2.x[1]):
            return True
        else:
            return False

p1 = Point(1, 3)
p2 = Point(3, 1)
r1 = Rectangle(p1, p2)
print(r1.get_area())
print(r1.get_perimeter())
print(r1.is_square())


p3 = Point(3, 7)
p4 = Point(6, 4)
r2 = Rectangle(p3, p4)
print(r2.get_area())
print(r2.get_perimeter())
print(r2.is_square())
