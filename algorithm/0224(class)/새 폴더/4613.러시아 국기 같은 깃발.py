T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    flag = [list(input()) for _ in range(N)]

    minV = 2500
    for i1 in range(0, N-2):
        for i2 in range(i1+1, N-1):
            cnt = N*M
            
            for i in range(0, i1+1):
                cnt -= flag[i].count('W')
                
            for i in range(i1+1, i2+1):
                cnt -= flag[i].count('B')

            for i in range(i2+1, N):
                cnt -= flag[i].count('R')

            if minV > cnt:
                minV = cnt

    print(f'#{tc} {minV}')