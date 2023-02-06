import sys

sys.stdin = open('paint.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    F = [[0]*10 for y in range(10)]
    for i in range(N):
        p = list(map(int, input().split()))
        print(p)
        for aa in range(p[0], p[2]+1):
            for k in range(p[1], p[3]+1):
                if F[aa][k] == 0 or F[aa][k] == p[4]:
                    F[aa][k] = p[4]
                else:
                    F[aa][k] = 3
    cnt = 0
    for yy in F:
        for ii in yy:
            if ii == 3:
                cnt += 1
    print(f'#{tc} {cnt}')
