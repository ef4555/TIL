'''
다음은 연결되어있는 두 개의 정점 사이의 간선을 순서대로 나열 해 놓은 것이다. 모든 정점을 깊이 우선 탐색하여
화면에 깊이 우선 탐색 경로를 출력하시오. 시작 정점을 1로 시작하시오
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7

출력 예)
1-2-4-6-5-7-3
'''

#   A B C D E F G
# A 0 1 1 0 0 0 0    1
# B 1 0 0 1 1 0 0    2
# C 1 0 0 0 0 0 1    3
# D 0 1 0 0 0 1 0    4
# E 0 1 0 0 0 1 0    5
# F 0 0 0 1 1 0 1    6
# G 0 0 1 0 0 1 0    7

#   1 2 3 4 5 6 7

V, E = map(int, input().split()) # 정점수, 이어진 선 개수
arr = list(map(int, input().split()))
adjM = [[0]*(V+1) for _ in range(V+1)] # 인덱스에 접근 편하게 하기 위해 V+1만큼의 크기로 만듦
adjL = [[0] for _ in range(V+1)] # 방문 이후 체크하는 adjL

for i in range(E):
    v1, v2 = arr[i*2], arr[i*2+1] # 01, 23, 34

    adjM[v1][v2] = 1
    adjM[v2][v1] = 1

    adjL[v1].append(v2)
    adjL[v2].append(v1)

for k in range(1, V+1):
    print(*adjM[k][1:V+1])
