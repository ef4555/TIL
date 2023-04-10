def bfs(a, N):
    visited = [0] * (N + 1)  # N: 정점의 개수
    q = [a] # 시작점을 인큐
    visited[a] = 0  # 시작점 0으로 표시
    while q :               # 큐가 비어있지 않으면
        t = q.pop(0)  # 디큐
        for i in range(N+1):  # 0부터 6까지 확인하며
            if visited[i] == 0 and arr[t][i] == 1:  # 방문되지 않은 곳이고, t 점과 이어진 노드면
                q.append(i)  # 큐에 넣기
                visited[i] = visited[t] + 1  # t에서 1만큼 증가해서 넣기(이동거리)
    call_max_list = []
    for k in list(enumerate(visited)): # 인덱스 번호와 연락 횟수 묶어서 꺼낸다
        if k[1] == max(visited): # visited가 누적이 되므로 visted의 최댓값 가진 노드가 가장 나중에 연락받은 노드
            call_max_list.append(k) # 리스트에 저장
    return call_max_list[-1][0] # 가장 나중에 연락받은 노드 중 번호가 제일 큰 노드 반환





import sys
sys.stdin = open('input (1).txt')
T = 10
for tc in range(1, T+1):
    E, S = map(int, input().split())
    arr = [[0] * (101) for _ in range(101)]  # 연결된 상태를 저장할 리스트
    lst = list(map(int, input().split())) # 연결 정보를 받을 리스트
    # print(lst)
    i = 0
    while 2*i+1 <= E-1: # 2씩 늘리면서 arr에 저장
        n1, n2 = lst[2*i], lst[2*i+1]
        arr[n1][n2] = 1
        i += 1
    ans = bfs(S, 100)
    print(f'#{tc} {ans}')