import sys
sys.stdin = open('input.txt')
from collections import deque

# 현재 위치에서 먹을 수 있는 물고기 찾고 최단거리 구함 BFS
# 먹은 물고기의 위치로 이동, 시간 갱신, 아기상어 크기 증가했는지 확인
# 다시 BFS로 먹을 수 있는 다른 물고기 탐색
# 먹을 수 있는 물고기가 없으면 = fish리스트에 아무것도 없으면
# 탐색 종료 ans 

def bfs(i, j):
    q = deque([])
    q.append([i,j]) 
    visited = [[0]*N for _ in range(N)]
    distance = [[0 for _ in range(N)] for _ in range(N)]
    fish = []
    global ss
    while q:
        i,j = q.popleft()
        for k in range(4):
            ni = i + d[k][0]
            nj = j + d[k][1]
            if 0 <= ni < N  and 0 <= nj < N and visited[ni][nj] == 0 and arr[ni][nj] <= ss:
                    visited[ni][nj] = 1
                    distance[ni][nj] = distance[i][j] + 1 
                    q.append([ni,nj]) 
                    if arr[ni][nj] < ss and arr[ni][nj] != 0: #물고기가 있고 그걸 먹을 수 있다면
                            fish.append([ni, nj, distance[ni][nj]])
    fish.sort(key = lambda x : (x[2], x[0], x[1])) # 거리 가까운 순서, 위쪽에 있는 순서, 왼쪽에 있는 순서로 정렬
    return fish


N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]
for i in range(N):
    for j in range(N):
        if arr[i][j] == 9:
            arr[i][j] = 0
            si, sj = i, j


d = ((-1,0), (1,0), (0,-1), (0,1)) # 상하좌우
ss = 2 # 물고기 크기
move = 0 # 이동 횟수(시간)
ans = 0
sharkeat = 0 # 먹은 물고기


while True:
    fishlist = bfs(si,sj)

    if len(fishlist) == 0: # 먹을 수 있는 물고기가 없다면
        print(ans)
        break

    si, sj, move = fishlist[0] # 먹을수 있는 물고기 중 우선순위 제일 먼저인 물고기의 위치로 이동
    sharkeat += 1
    if ss == sharkeat: # 크기만큼의 물고기 마리수를 먹으면 성장
        sharkeat = 0
        ss += 1 # 크기 증가

    arr[si][sj] = 0 # 물고기 먹은 자리는 빈칸으로 바꿈
    ans += move
