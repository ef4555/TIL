> 비선형구조인 그래프 구조는 표현된 모든 자료를 빠짐없이 탐색하는 것이 중요! 그래서 아래와 같은 탐색 기법이 존재한다.  
> 
> 1. DFS
> 2. BFS 

"내가 다시 돌아올 곳을 저장"
    - 가장 마지막에 만났던 갈림길 간선이 있는 정점으로 되돌아와서 다른 방향의 정점으로 계속 반복 탐색하여, 모든 정점을 탐색한다. 
    - 스택의 후입선출 구조 또는 재귀호출을 통해서 구현하게됩니다. 

### 그래프를 표현하는 방법 (인접행렬)

1. 딕셔너리의 활요 
   
   ```python
   graph = {}
   ```

graph['A'] = ['B', 'C']
graph['B'] = ['D', 'F']
.
.
.
.
.
.

```
3. 2차원 배열의 활용
```python

#   A B C D E F
# A 0 1 1 0 0 0
# B 0 0 0 1 0 1   
# C
# D
# E
# F
```

- 코드로 구현하기 
  
  ```python
  
  ```

'''
7 8  V, E 
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
'''

# V(정점), E(간선)

V, E = map(int, input().split())

data = list(map(int, input().split()))

arr = [[0] * (V + 1) for _ in range(V + 1)]

visited = [0] * (V+1) # 방문 여부 확인하는 List

for i in range(E):
    n1, n2 = arr[i*2], arr[i*2+1]
    arr[n1][n2] = 1 # n1 과 n2는 인접해있다. 
    arr[n2][n1] = 1

```
- 탐색해보기 
``` python 

def dfs(v):
    visited[v] = 1
    print(v, end = " ")
    # 현재 v는 시작정점, 인접한 정점 중 방문을 안한 곳 
    for w in range(1, V+1):
        if arr[v][w] == 1 and visited[w] == 0:
            dfs(w)


dfs(1)
```



반복문으로 dfs 구현하기 

```python
def dfs(v):

    stack = [v]
    # stack.append(v)
    # 스택이 빌 때까지 반복 
    while len(stack):
        v = stack.pop()
        # v가 아직 방문 전이라면 
        visited[v] = 1

        for w in range(1, V + 1):
        if arr[v][w] == 1 visited[w] == 0:
            stack.append(w)
```