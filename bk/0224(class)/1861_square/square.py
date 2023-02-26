def bfs(si, sj):
    q = []  # [0] 생성
    alst = [] # 

    q.append((si, sj))  # [1] 초기데이터 삽입
    v[si][sj] = 1
    alst.append(arr[si][sj])

    while q:
        ci, cj = q.pop(0)

        # 4방향, 미방문, 조건 맞으면!! (1차이)
        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ni, nj = ci + di, cj + dj
            if 0 <= ni < N and 0 <= nj < N and v[ni][nj] == 0 and \
                    abs(arr[ci][cj] - arr[ni][nj]) == 1:
                q.append((ni, nj)) # 방의 좌표 저장
                v[ni][nj] = 1 
                alst.append(arr[ni][nj]) # 방의 넘버 저장

    return min(alst), len(alst) # 순회했던 방중에 최소 넘버는 시작한 방, alst의 길이는 이동한 방 개수


T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    v = [[0] * N for _ in range(N)]
    ans, cnt = N * N, 0 # 처음에 출발해야 하는 방, 몇 개의 방을 이동할 수 있는지
    for si in range(N):
        for sj in range(N):
            if v[si][sj] == 0:
                t, tcnt = bfs(si, sj) 
                if cnt < tcnt or cnt == tcnt and ans > t:
                    ans, cnt = t, tcnt

    print(f'#{test_case} {ans} {cnt}')
