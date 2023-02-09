class Stack:
    def __init__(self):
        self.lst = []

    def empty(self):
        if len(self.lst) == 0:
            return True
        else:
            return False

    def top(self):
        if len(self.lst) == 0:
            return None
        else:
            return self.lst[-1]
    
    def pop(self):
        if len(self.lst) == 0:
            return None
        else:
            return self.lst.pop(-1)

    def push(self, num):
        return self.lst.append((num))

    def __repr__(self):
        return self.lst


s = Stack()
print(s.top())
print(s.push(1))
print(s.push(2))
print(s.push(3))
print(s.top())
print(s.empty())
print(s.__repr__())
print(s.pop())
print(s.__repr__())
print(s.pop())
print(s.pop())
print(s.pop())

