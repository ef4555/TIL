from collections import deque
import sys
input = sys.stdin.readline


q = deque([])
N = int(input())
for _ in range(N):
    m = input().split()
    if m[0] == 'push':
        q.append(m[1])
    elif m[0] == 'pop':
        if q:
            print(q.popleft())
        else:
            print(-1)
    elif m[0] == 'size':
        print(len(q))
    elif m[0] == 'empty':
        if q:
            print(0)
        else:
            print(1)
    elif m[0] == 'front':
        if q:
            print(q[0])
        else:
            print(-1)
    elif m[0] == 'back':
        if q:
            print(q[-1])
        else:
            print(-1)
