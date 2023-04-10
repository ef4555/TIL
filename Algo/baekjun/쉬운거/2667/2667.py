import sys
sys.stdin = open("input.txt")

from collections import deque



N = int(input())

arr = [list(map(int, list(input()))) for _ in range(N)]

visited = [[0]*N for _ in range(N)]

adr = [[] for _ in range(N*N)]
house = 0

def address(house, visited, arr):
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 1 and visited[i][j] == 0:
                house += 1 # 단지 시작지점 찾으면 + 1
                queue = deque([[i, j]])
                visited[i][j] = 1
                adr[house].append([i, j])
                # print(queue)
                
                while queue:
                    x, y = queue.popleft()
                    for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
                        nx = x + dx
                        ny = y + dy
                        if 0 <= nx < N and 0 <= ny < N and arr[nx][ny] == 1 and visited[nx][ny] == 0:
                            visited[nx][ny] = 1
                            adr[house].append([nx, ny])
                            queue.append([nx, ny])
                            # print(queue)
                            # print(adr)
    
    return (house, visited, arr)

house, visited, arr = address(house, visited, arr)

print(house)
lst = []
for i in range(1, house+1):
    lst.append(len(adr[i]))
lst.sort()
for k in lst:
    print(k)