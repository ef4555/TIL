import sys
sys.stdin = open('zick.txt')
for _ in range(4):
    lst = list(map(int, input().split()))
    a = lst[:2]
    b = lst[2:4]
    print(a, b)
    c = lst[4:6]
    d = lst[6:8]
    print(c, d)

