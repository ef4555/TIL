from collections import deque
import sys
input = sys.stdin.readline


s = deque([])
N = int(input())
for _ in range(N):
    m = input().split()
    if m[0] == 'push':
        s.append(m[1])
    elif m[0] == 'pop':
        if s:
            print(s.pop())
        else:
            print(-1)
    elif m[0] == 'size':
        print(len(s))
    elif m[0] == 'empty':
        if s:
            print(0)
        else:
            print(1)
    elif m[0] == 'top':
        if s:
            print(s[-1])
        else:
            print(-1)
