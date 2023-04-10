'''
import sys
sys.stdin = open('p2.txt')
T = 6
for tc in range(1, T+1):
    N = input()
    moon_lst = []
    for i in N:
        moon_lst.append(i)
    print(f'#{tc}', ''.join(moon_lst), type(''.join(moon_lst)))
'''


import sys
sys.stdin = open('p2.txt')
T = 6
s = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
for tc in range(1, T+1):
    N = input()
    moon_lst = []
    m = int(N)
    if m < 0:
        m = -m
    while m != m//10:
        y = m % 10
        moon_lst.append(y)
        m = m//10
    lst = moon_lst[::-1]
    l = []
    for i in lst:
        if i >= 0:
            l.append(s[i])
        if i < 0:
            l.append(s[(-i)])
    print(f'#{tc}', ''.join(l), type(''.join(l)))






