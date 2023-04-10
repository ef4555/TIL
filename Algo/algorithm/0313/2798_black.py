import sys
sys.stdin = open('test.txt')
N, M = map(int, input().split())
lst = list(map(int, input().split()))
# print(lst)
max_m = 0
for i in range(N-2):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            if (lst[i]+lst[j]+lst[k]) > M:
                continue
            else:
                r = (lst[i]+lst[j]+lst[k])
                if max_m <= r:
                    max_m = r
print(max_m)
