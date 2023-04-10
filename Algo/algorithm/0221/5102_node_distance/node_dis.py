def bfs(a, b, N):
    visited = [0] * (N + 1)  # N: 정점의 개수
    q = [a] # 시작점을 인큐
    visited[a] = 0  # 시작점 0으로 표시
    while q :               # 큐가 비어있지 않으면
        t = q.pop(0)  # 디큐
        for i in range(N+1):  # 0부터 6까지 확인하며
            if visited[i] == 0 and arr[t][i] == 1:  # 방문되지 않은 곳이고, t 점과 이어진 노드면
                q.append(i)  # 큐에 넣기
                visited[i] = visited[t] + 1  # t에서 1만큼 증가해서 넣기(이동거리)

    if visited[G] != 0: # 도착점에 도달했다면
        return visited[G] # 이동거리 반환
    else: # 다 돌았는데도 G에 visited 찍지 못했으면
        return 0


import sys
sys.stdin = open('sample_input.txt')
T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    arr = [[0] * (V + 1) for _ in range(V + 1)]
    for i in range(E):
        data = list(map(int, input().split()))
        n1, n2 = data[0], data[1]
        arr[n1][n2] = 1
        arr[n2][n1] = 1
    S, G = map(int, input().split())
    ans = bfs(S, G, V)
    print(f'#{tc} {ans}')

