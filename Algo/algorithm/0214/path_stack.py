'''
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7



#   A B C D E F G
# A 0 1 1 0 0 0 0    1
# B 1 0 0 1 1 0 0    2
# C 1 0 0 0 0 0 1    3
# D 0 1 0 0 0 1 0    4
# E 0 1 0 0 0 1 0    5
# F 0 0 0 1 1 0 1    6
# G 0 0 1 0 0 1 0    7

#   1 2 3 4 5 6 7
'''

V, E = map(int, input().split())
data = list(map(int, input().split()))
arr = [[0] * (V + 1) for _ in range(V + 1)] # 인덱스에 접근 편하게 하기 위해 정점 V보다 하나 많게 만듦

visited = [0] * (V+1) # 방문 이후 확인하는 List

for i in range(E):
  n1, n2 = data[i*2], data[i*2+1] # 데이터에서 인접한 부분 정보 불러와서 변수에 저장0 1, 2 3, 4 5
  arr[n1][n2] = 1 # n1과 n2는 인접해있다.
  arr[n2][n1] = 1 # n1과 n2는 인접해있다. 연습 코드에서는 방향이 없으므로 서로 이어주어야 한다.

# 탐색해보기
def dfs(v):
  visited[v] = 1
  print(v, end = " ")
  # 현재 v는 시작 정점, 인접한 정점 중 방문을 안한 곳
  for w in range(1, V+1):
    if arr[v][w] == 1 and visited[w] == 0:
      dfs(w)

  print('aaaaaaaaaa')

dfs(1)