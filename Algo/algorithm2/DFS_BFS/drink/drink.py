import sys
sys.stdin = open('input.txt')

# 안찍힌 점을 발견하면
# 군집 카운트를 +=1 하고 
# 그 점과 연결된 모든 점을 체크표시함

N, M = map(int, input().split())
arr = []
for i in range(N):
    arr.append(list(map(int, input())))
d = ((-1,0),(1,0),(0,-1),(0,1)) # 상하좌우
def dfs(i, j):
    if i <= -1 or i >= N or j <= -1 or j >= M:
        return False
    if arr[i][j] == 0:
        arr[i][j] = 1
        for k in range(4):
            dfs(i+d[k][0], j+d[k][1])
        return True
    
    return False

ans = 0
for ii in range(N):
    for jj in range(M):
        if dfs(ii,jj) == True:
            ans += 1
print(ans)