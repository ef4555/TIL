import sys
sys.stdin = open('big.txt')
lst = []
kk = 0
while kk == 0:
    A, B = map(int, input().split())
    if A == 0 and B == 0:
        kk = 1
        break
    else:
        if A > B:
            print("YES")
        else:
            print("NO")

