import sys
sys.stdin = open('input.txt')
from collections import deque

N, M = map(int, input().split())
arr = []
for i in range(N):
    arr.append(list(map(int, input())))
visited = [[0]*M for _ in range(N)]
visited[0][0] = 1
q = deque([])
q.append([0,0])
d = ((-1,0),(1,0),(0,-1),(0,1))
while q:
    a = q.popleft()
    for k in range(4):
        ni = a[0] + d[k][0]
        nj = a[1] + d[k][1]
        if 0<= ni < N and 0<= nj < M and visited[ni][nj] == 0 and arr[ni][nj] != 0:
            q.append([ni,nj])
            visited[ni][nj] = visited[a[0]][a[1]] + 1
print(visited[N-1][M-1])
    
