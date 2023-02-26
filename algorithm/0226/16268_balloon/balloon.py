import sys
sys.stdin = open('input1.txt')
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # print(arr)
    d = ((-1,0), (1,0), (0,-1), (0,1)) # 상하좌우
    b_max = 0
    for i in range(N):
        for j in range(M):
            cnt = arr[i][j]
            for k in range(4):
                ni = i + d[k][1]
                nj = j + d[k][0]
                if 0 <= ni < N and 0 <= nj < M:
                    cnt += arr[ni][nj]
            if b_max <= cnt:
                b_max = cnt
    print(f'#{tc} {b_max}')


