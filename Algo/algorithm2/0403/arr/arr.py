'''
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
'''

V, E = map(int, input().split())
arr = list(map(int,input().split()))
adjm = [[0]*(V+1) for _ in range(V+1)]
adjl = [[0] for _ in range(V+1)]
for i in range(E): # E개의 간선 순회하면서
    n1, n2 = arr[i*2], arr[i*2 + 1]
    adjm[n1][n2] = 1
    adjm[n2][n1] = 1
    adjl[n1].append(n2)
    adjl[n2].append(n1)
print(adjm)
print(adjl)