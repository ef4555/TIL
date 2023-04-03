def dfs(n):
    global ans
    if n == N:
        ans += 1
        return
    for j in range(N):
        if v1[j]==v2[n]
            


N = int(input())
ans = 0
v1, v2, v3 = [[0]*(2*N) for _ in range(3)]
dfs(0)
arr = [[0]*N for _ in range(N)]
# 퀸을 놓고 다음 퀸을 놓을 수 있는 좌표 구하고 그 좌표들 중 하나 선택해서 
# 퀸 놓고 카운트 하나 줄이고