import sys
sys.stdin = open('ship.txt')
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split()) # 구역의 크기
    arr = [list(map(int, input().split())) for _ in range(N)]
    print(arr)
    d = [[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]] # 8방향 델타탐색
    hoobo = 0
    for ii in range(N):
        for jj in range(M):
            cnt = 0
            for k in range(8):
                ni = ii + d[k][0]
                nj = jj + d[k][1]
                if 0 <= ni < N and 0 <= nj < M:
                    if arr[ni][nj] < arr[ii][jj]:
                        cnt += 1
            if cnt >= 4:
                hoobo += 1
    print(f'#{tc} {hoobo}')

