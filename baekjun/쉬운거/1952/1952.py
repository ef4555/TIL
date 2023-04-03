d = ((0,1), (1,0), (0,-1), (-1,0)) # 우 하 좌 상

M, N = map(int,input().split())
arr = [[0]*N for _ in range(M)]
dr = 0
arr[0][0] = 1
i = 0
j = 0
cnt = 1
ans = 0
while cnt < N*M:
    ni = i + d[dr][0]
    nj = j + d[dr][1]
    if 0<=ni<M and 0<=nj< N and arr[ni][nj]==0:
        arr[ni][nj] = 1
        i, j = ni, nj
        cnt += 1
    else:
        ans += 1
        dr = (dr+1)%4
        ni = i + d[dr][0]
        nj = j + d[dr][1]
        if 0<=ni<M and 0<=nj< N and arr[ni][nj]==0:
            arr[ni][nj] = 1
            i, j = ni, nj
            cnt += 1

print(ans)

