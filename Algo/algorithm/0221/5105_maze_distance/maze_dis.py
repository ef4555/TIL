'''
NxN 크기의 미로에서 출발지 목적지가 주어진다.

이때 최소 몇 개의 칸을 지나면 출발지에서 도착지에 다다를 수 있는지 알아내는 프로그램을 작성하시오.

경로가 있는 경우 출발에서 도착까지 가는데 지나야 하는 최소한의 칸 수를, 경로가 없는 경우 0을 출력한다.

다음은 5x5 미로의 예이다. 1은 벽, 0은 통로를 나타내며 미로 밖으로 벗어나서는 안된다.

13101
10101
10101
10101
10021

마지막 줄의 2에서 출발해서 0인 통로를 따라 이동하면 맨 윗줄의 3에 5개의 칸을 지나 도착할 수 있다.


[입력]

첫 줄에 테스트 케이스 개수 T가 주어진다.  1<=T<=50

다음 줄부터 테스트 케이스의 별로 미로의 크기 N과 N개의 줄에 걸쳐 미로의 통로와 벽에 대한 정보가 주어진다. 5<=N<=100

0은 통로, 1은 벽, 2는 출발, 3은 도착이다.

[출력]

각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.
'''
def bfs(a, b, N):
    q = [[a,b]]
    while q :               # 큐가 비어있지 않으면
        t = q.pop(0)  # 디큐
        for k in range(4): # 디큐해서 나온 좌표에서 4방향 델타탐색
            ni = t[0] + di[k] # 새로운 좌표
            nj = t[1] + dj[k]
            if 0 <= ni < N and 0 <= nj < N: # 범위 안에 있으면
                if lst[ni][nj] != 1 and visited[ni][nj] == 0: # 벽이 아니고 방문한 곳이 아니면
                    if lst[ni][nj] == 3: # 3이 나왔을 경우 그 전 좌표의 거리값 반환
                        return visited[t[0]][t[1]]
                        break
                    else:
                        q.append([ni, nj])
                        visited[ni][nj] = visited[t[0]][t[1]] + 1  # v 인큐되었음 표시, 거리
    return 0

import sys
sys.stdin = open('sample_input (1).txt')
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    lst = [list(map(int, input()[:N])) for _ in range(N)]

    di = [-1, 0, 1, 0] # 상 0 하 0
    dj = [0, 1, 0, -1] # 0 우 0 좌
    si = 0
    sj = 0
    for q in range(N):
        for z in range(N):
            if lst[q][z] == 2:
                si = q
                sj = z
    # print(si, sj)

    visited = [[0] * (N) for _ in range(N)]
    visited[si][sj] = 0 # 시작점 거리를 0으로 설정
    ans = bfs(si, sj, N) # 함수 실행해서 반환값 저장

    print(f'#{tc} {ans}')
