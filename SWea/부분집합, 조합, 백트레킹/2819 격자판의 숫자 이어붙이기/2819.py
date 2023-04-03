
def dfs(x, y, num):
    global ans
    # 종료 조건
    if len(num) == 7:
        ans.add(num) # ans에 값 넣음, 중복 제거됨
        return
    
    # 상하좌우 이동
    delta = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    for dx, dy in delta:
        nx, ny = x + dx, y + dy
        # 격자판 범위 내에 있고, 아직 방문하지 않은 곳이면 dfs 호출
        if 0 <= nx < 4 and 0 <= ny < 4:
            dfs(nx, ny, num + arr[nx][ny])



T = int(input())
for tc in range(1, T+1):
    arr = [input().split() for _ in range(4)]
    ans = set()
    for i in range(4):
        for j in range(4):
            dfs(i, j, arr[i][j])
    print(f"#{tc} {len(ans)}")