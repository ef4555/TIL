'''
NxN 크기의 미로에서 출발지에서 목적지에 도착하는 경로가 존재하는지 확인하는 프로그램을 작성하시오. 도착할 수 있으면 1, 아니면 0을 출력한다.

주어진 미로 밖으로는 나갈 수 없다.

다음은 5x5 미로의 예이다.

13101

10101

10101

10101

10021


마지막 줄의 2에서 출발해서 0인 통로를 따라 이동하면 맨 윗줄의 3에 도착할 수 있는지 확인하면 된다.


[입력]


첫 줄에 테스트 케이스 개수 T가 주어진다.  1<=T<=50


다음 줄부터 테스트 케이스의 별로 미로의 크기 N과 N개의 줄에 걸쳐 미로의 통로와 벽에 대한 정보가 주어진다. 0은 통로, 1은 벽, 2는 출발, 3은 도착이다. 5<=N<=100


[출력]

각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 계산결과를 정수로 출력하거나 또는 ‘error’를 출력한다.
'''
import sys
sys.stdin = open('maze.txt')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    lst = [[0] * (N) for _ in range(N)] # 미로의 정보를 받을 리스트
    for p in range(N):
        lst[p] = list(map(int, input()[:N])) # 미로 정보 lst에 넣기
    di = [-1, 0, 1, 0]  # 상 0 하 0
    dj = [0, 1, 0, -1]  # 0 우 0 좌
    si = 0
    sj = 0
    for q in range(N): # 시작점을 찾음
        for z in range(N):
            if lst[q][z] == 2:
                si = q
                sj = z
    # print(si, sj)
    ei = 0
    ej = 0
    for qq in range(N): # 3인 도착점을 찾음
        for zz in range(N):
            if lst[qq][zz] == 3:
                ei = qq
                ej = zz
    # print(ei, ej)
    visited = [[0] * (N) for _ in range(N)] # 방문한 지점 기록
    stack = []
    stack.append([si, sj])
    visited[si][sj] = 1
    result = 0
    while stack:  # 스택에 이동 가능 지점이 있을 때까지, 해당 지점이 이동 불가능 점이면 pop, 이동경로를 스택에 넣는 느낌
        x, y = stack.pop()
        visited[x][y] = 1
        for i in range(4):
            nx = x + di[i]
            ny = y + dj[i]
            # 경계 검사
            if nx < 0 or nx == N or ny < 0 or ny == N:
                continue
            # 이동

            if lst[nx][ny] == 3:
                result = 1
                break
            elif not lst[nx][ny] and not visited[nx][ny]:  # 0일 경우 이동경로에 추가
                stack.append((nx, ny))


    print(lst)
    print(visited)
    print(f'#{tc} {result}')