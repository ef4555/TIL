'''
6 11
0 1 32
0 2 31
0 5 60
0 6 51
1 2 21
2 4 46
2 6 25
3 4 34
3 5 18
4 5 40
4 6 51
'''

def find_set(x): # x가 속한 집합의 대표원소 리턴
    while x != rep[x]: # x == rep[x]가 까지
        x = rep[x]
    return x        
    
def union(x, y): # y의 대표원소가 x의 대표원소를 가리키도록 함
    rep[find_set(y)] = find_set(x)
    rep[y] = find_set(x)
    
V, E = map(int, input().split())
rep = [i for i in range(V+1)]
graph = []
for _ in range(E):
    v1, v2, w = map(int, input().split())
    graph.append([v1, v2, w])

# 가중치 기준 오름차순 정렬
graph.sort(key=lambda x:x[2])
print(graph)
# N개의 정점(V+1), N-1개의 간선 선택
N = V+1
s = 0   # MST에 포함된 간선의 가중치 합
cnt = 0
for v, u, w, in graph: # 가중치가 작은 것부터
    if find_set(u) != find_set(v): # 사이클이 생기지 않으면(대표원소가 다르면 서로 떨어져 있는 상태)
        s += w # 가중치 합
        union(u, v)
        if cnt == N-1: # MST 구성 완료
            break
print(s)
