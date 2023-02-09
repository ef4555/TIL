

def sum_of_digit(a):
    s_di = 0
    for i in str(a):
        s_di += int(i)
    return s_di

'''
def sum_of_digit(a):
    b = list(str(a))
    c = list(map(int, b))
    return sum(c)
'''

sum_of_digit(3904) # 16
