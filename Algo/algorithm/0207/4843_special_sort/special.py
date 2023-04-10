import sys
sys.stdin = open('special.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    a = list(map(int, input().split()))
    for i in range(N-1):
        Idx = i
        if i%2 == 0 :
            for j in range(i+1, N):
                if a[Idx] < a[j]:
                    Idx = j
            a[i], a[Idx] = a[Idx], a[i]
        elif i%2 == 1:
            for j in range(i+1, N):
                if a[Idx] > a[j]:
                    Idx = j
            a[i], a[Idx] = a[Idx], a[i]
    print(f'#{tc}', *a[0:10])