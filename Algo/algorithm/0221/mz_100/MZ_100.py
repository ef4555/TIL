def bfs(a, b, N):
    q = [[a,b]]
    while q :               # 큐가 비어있지 않으면
        t = q.pop(0)  # 디큐(선입선출)
        for k in range(4): # 디큐해서 나온 좌표에서 4방향 델타탐색
            ni = t[0] + di[k] # 새로운 좌표
            nj = t[1] + dj[k]
            if 0 <= ni < N and 0 <= nj < N: # 범위 안에 있으면
                if maze[ni][nj] != 1 and visited[ni][nj] == 0: # 벽이 아니고 방문한 곳이 아니면
                    if maze[ni][nj] == 3: # 3이 나왔을 경우 끝내고 1 반환
                        return 1
                    else:
                        q.append([ni, nj]) # 통로 좌표 인큐(큐의 맨 뒤로 가게 됨)
                        visited[ni][nj] = 1  # visited 표시
    return 0 # 반복 다 돌았는데 3으로 못 닿았을 경우


import sys
sys.stdin = open('sample_input.txt')
T = 10
for _ in range(1, T+1):
    tc = int(input())
    maze = [list(map(int, input())) for _ in range(100)]
    si = sj = 1 # 시작점 (1,1)
    di = [-1, 0, 1, 0] # 상 0 하 0
    dj = [0, 1, 0, -1] # 0 우 0 좌
    visited = [[0] * (100) for _ in range(100)]
    visited[si][sj] = 1 # 시작점 체크
    ans = bfs(si, sj, 100)  # 함수 실행해서 반환값 저장
    print(f'#{tc} {ans}')