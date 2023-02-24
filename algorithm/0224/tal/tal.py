p = [[], [0, 1, 2, 3], [0, 1], [2, 3], [0, 3], [1, 3], [1, 2], [0, 2]] # 상하좌우 일단 0123으로 할당
opp = {0: 1, 1: 0, 2: 3, 3: 2} # 상이면 하랑, 하면 상이랑, 좌면 우랑, 우면 좌랑 연결이 되어있어야함
di, dj = [-1, 1, 0, 0], [0, 0, -1, 1]  # 상하좌우 표시


def bfs(si, sj, l):
    q = []
    v = [[0] * m for _ in range(n)]  # 가로 세로 다를 때 특히 주의

    q.append((si, sj))
    v[si][sj] = 1
    cnt = 1

    while q:
        ci, cj = q.pop(0)
        if v[ci][cj] == l:
            return cnt

        for dr in p[arr[ci][cj]]: # 파이프가 연결된 부분만 탐색
            ni, nj = ci + di[dr], cj + dj[dr] # 연결된 부분에 따라서 상하좌우 할당
            # 범위 안이고, 안 간곳이고, 현재 연결된 부분에 다음 파이프가 연결되는지 확인(다음파이프의 방향중에 있는지(in))
            if 0 <= ni < n and 0 <= nj < m and v[ni][nj] == 0 and opp[dr] in p[arr[ni][nj]]:
                q.append((ni, nj))
                v[ni][nj] = v[ci][cj] + 1 # 누적해서 적어줌
                cnt += 1 # 탈주범이 있을 수 있는 장소 개수 추가
    # 공간이 좁아서 L일전에 모두 방문
    return cnt


t = int(input())
for tc in range(1, t + 1):
    n, m, r, c, l = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]

    ans = bfs(r, c, l)
    print(f'#{tc} {ans}')