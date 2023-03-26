from collections import deque
import sys

sys.stdin = open('7569.txt')
t_q = deque([])
M, N, H = map(int, input().split()) # M는 x축(j) N은 y축(i), H은 z축(z)
arr = [[list(map(int, input().split())) for _ in range(N)]  for _ in range(H)]
# print(arr)
d = ((1,0,0),(-1,0,0),(0,-1,0),(0,1,0),(0,0,-1),(0,0,1)) # 위아래 상하좌우 6방향
for z in range(H):
    for i in range(N):
        for j in range(M):
            if arr[z][i][j] == 1:
                t_q.append([z,i,j])
# print(t_q)

i = -1 # 빈 큐일때도 세게 되어서 -1로 시작
while t_q: # 큐 빌때까지
    i += 1
    # a += len(t_q)
    for _ in range(len(t_q)): # 새로 익은 토마토 만큼만 반복
        x = t_q.popleft()
        for k in range(6):
            nz = x[0] + d[k][0]
            ni = x[1] + d[k][1] # i는 y좌표
            nj = x[2] + d[k][2] 
            if 0 <= nz < H and 0 <= ni < N and 0 <= nj < M and arr[nz][ni][nj] == 0:
                t_q.append([nz,ni,nj])
                arr[nz][ni][nj] = 1 # 익은 토마토로 변경
cnt = i
for zz in range(H):
    for ii in range(N):
        for jj in range(M):
            if arr[zz][ii][jj] == 0:
                cnt = -1 # -1 발견하자마자 탈출
                break
print(cnt)

