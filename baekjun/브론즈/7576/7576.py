from collections import deque

import sys
sys.stdin = open('7576.txt')
M, N = map(int, input().split()) # M는 x축(j) N은 y축(i)
arr = [list(map(int, input().split())) for _ in range(N)]
d = ((-1,0),(1,0),(0,-1),(0,1)) # 상하좌우
t_q = deque([])
c = 0

# 처음에 pop(0)을 썼는데 시간초과
# t_q[0]으로 꺼내서 저장하고 지워도 시간초과
# deque 사용하니 통과

for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            t_q.append([i,j])
# print(t_q)
i = -1 # 빈 큐일때도 세게 되어서 -1로 시작
while t_q: # 큐 빌때까지
    i += 1
    # a += len(t_q)
    for _ in range(len(t_q)): # 새로 익은 토마토 만큼만 반복
        x = t_q.popleft()
        for k in range(4):
            ni = x[0] + d[k][0] # i는 y좌표
            nj = x[1] + d[k][1] 
            if 0 <= ni < N and 0 <= nj < M and arr[ni][nj] == 0:
                t_q.append([ni,nj])
                arr[ni][nj] = 1 # 익은 토마토로 변경
    # print(t_q)
# print(a)
# print(M*N-c)
# if a == M*N-c:
#     print(i)
# else:
#     print(-1)

cnt = i
for ii in range(N):
    for jj in range(M):
        if arr[ii][jj] == 0:
            cnt = -1 # -1 발견하자마자 탈출
            break
print(cnt)

