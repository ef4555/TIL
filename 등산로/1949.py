import sys
sys.stdin = open('input.txt')
from collections import deque
'''
def bfs(x, y, h):
    q = deque()
    q.append([x, y, h])
    while q:
        a, b, c = q.popleft() # a, b 좌표, c는 높이
        for l in range(4):
            na = a + d[l][0]
            nb = b + d[l][1]
            if 0 <= na < N and 0 <= nb < N and arr[na][nb] < c:
                # 범위 안이고 visited 체크 안되어있고 높이가 c보다 작으면
                q.append([na, nb, arr[na][nb]])
                visited[na][nb] = visited[a][b] + 1



'''
def bfs(x, y, h, t):
    q = deque()
    q.append([x, y, h])
    while q:
        a, b, c = q.popleft() # a, b 좌표, c는 높이
        for l in range(4):
            na = a + d[l][0]
            nb = b + d[l][1]
            if 0 <= na < N and 0 <= nb < N and arr[na][nb] - t < c:
                # 범위 안이고 visited 체크 안되어있고 높이가 c보다 작으면
                arr[na][nb] = arr[na][nb]-1
                q.append([na, nb, arr[na][nb]])
                t = 0
                visited[na][nb] = visited[a][b] + 1






T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    lst = []
    m_v = 0
    for k in range(N):
        if m_v <= max(arr[k]):
           m_v = max(arr[k])
    
    for i in range(N):
        for j in range(N):
            if arr[i][j] == m_v:
                lst.append([i,j,arr[i][j]])
    lst2 = []     
    print(lst)
    d = ((-1,0),(1,0),(0,-1),(0,1))
    for k in lst:
        visited = [[0]*N for _ in range(N)]
        ii, jj, kk = k
        visited[ii][jj] = 1
        
        bfs(ii, jj, kk, 1)
        print(visited)
        m = 0
        for k in range(N):
            if m <= max(visited[k]):
                m = max(visited[k])
        lst2.append(m)
    print(f'#{tc} {max(lst2)}')