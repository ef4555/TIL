import sys
sys.stdin = open('maze.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    lst = [[0] * (N) for _ in range(N)]
    for p in range(N):
        lst[p] = list(map(int, input()[:N]))
    di = [-1, 0, 1, 0] # 상 0 하 0
    dj = [0, 1, 0, -1] # 0 우 0 좌
    si = 0
    sj = 0
    for q in range(N):
        for z in range(N):
            if lst[q][z] == 2:
                si = q
                sj = z
    # print(si, sj)
    ei = 0
    ej = 0
    for qq in range(N):
        for zz in range(N):
            if lst[qq][zz] == 3:
                ei = qq
                ej = zz
    # print(ei, ej)
    visited = [[0] * (N) for _ in range(N)]
    visited[si][sj] = 1


    def dfs(a, b, c):
        for k in range(4):
            ni = a + di[k]
            nj = b + dj[k]
            if 0 <= ni < N and 0 <= nj < N:
                if lst[ni][nj] != 1 and visited[ni][nj] == 0:
                    visited[ni][nj] = 1
                    dfs(ni, nj, c)

    dfs(si, sj, N)
    # print(visited)
    if visited[ei][ej] == 1:
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')
