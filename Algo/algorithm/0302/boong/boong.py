import sys
sys.stdin = open('2.txt')

T = int(input())
for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    lst = list(map(int,input().split()))
    lst.sort()
    i = 0
    j = 0
    b = 0
    c = True
    while i <= 11111 :
        if i != 0:
            if i % M == 0:
                b += K
        if lst[j] == i:
            b -= 1
            if b < 0:
                c = False
                break
            if j == len(lst) - 1:
                break
            j += 1

        i += 1
    if c == True:
        print(f'#{tc} Possible')
    else:
        print(f'#{tc} Impossible')




