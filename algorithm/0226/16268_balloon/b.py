import sys
sys.stdin = open('input1.txt')
T = int(input())
for tc in range(1,T+1):
    N,M = map(int,input().split())
 
    total = list()
 
    result = list()
 
    for _ in range(N):
        a = list(map(int,input().split()))
        total.append(a)
 
    for i in range(N):
        for j in range(M):
            now = total[i][j]
            for mul_x,mul_y in [(1,0),(-1,0),(0,1),(0,-1)]:
                for k in range(1,total[i][j]+1):
                    nx = i +mul_x * k
                    ny = j +mul_y * k
 
                    if 0<=nx<N and 0<=ny<M:
                        now += total[nx][ny]
 
            result.append(now)
 
    print(f'#{tc} {max(result)}')