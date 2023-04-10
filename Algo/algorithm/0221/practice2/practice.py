'''
모든 정점을 너비우선탐색하여 경로를 출력
시작 정점은 1

7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7

'''
def bfs(v, N):
    visited = [0] * (N+1) # visited 생성
    q = [v]                # 큐 생성
                            # 시작점 인큐
    visited[v] = 1          # 시작점 인큐표시
    while q :               # 큐가 비어있지 않으면
        t = q.pop(0)        # 디큐
        print(t, end = ' ') # t에서 처리할 일
        for v in arr[t]:# t에 인접이고 방문한 적 없는 v
            if visited[v] == 0:
                q.append(v)                  # v 인큐
                visited[v] = visited[t] + 1  # v 인큐되었음 표시, 거리
    print(visited)

V, E = map(int, input().split()) # V 는 정점, E 는 연결선 수
data = list(map(int, input().split()))
arr = [[] for _ in range(V + 1)] # 인접 노드
visited = [0] * (V+1) # 인덱스 맞춰준다. A가 1부터
for i in range(E):
    n1, n2 = data[i*2], data[i*2+1] # 데이터에서 인접한 부분 정보 불러와서 변수에 저장0 1, 2 3, 4 5
    arr[n1].append(n2)  # n1과 n2는 인접해있다.
    arr[n2].append(n1)  # n1과 n2는 인접해있다. 연습 코드에서는 방향이 없으므로 서로 이어주어야 한다.
print(arr)
bfs(1, V)
