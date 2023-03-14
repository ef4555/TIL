T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    lst = [list(map(int, input().split())) for _ in range(N)]
    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]
    result_lst = []

    for y in range(N):
        for x in range(M):

            anw = lst[y][x]

            for k in range(4):
                for mul in range(1, lst[y][x]+1):
                    ni, nj = y + di[k] * mul, x + dj[k] * mul
                    if 0 <= ni < N and 0 <= nj < M:
                        anw += lst[ni][nj]
                    
            result_lst.append(anw)

    print(f'#{tc} {max(result_lst)}')
'''
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    mx = 0
    for i in range(N):
        for j in range(M):
            ans = arr[i][j]
            for di, dj in ((-1,0), (0,1), (1,0), (0,-1)):
                for mul in range(1, arr[i][j]+1):
                    ni, nj = i+di*mul, j+dj*mul
                    if 0 <= ni < N and 0 <= nj < M:
                        ans += arr[ni][nj]
            if ans > mx:
                mx = ans
    print(f'#{tc} {mx}')
    '''