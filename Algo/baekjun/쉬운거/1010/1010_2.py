
# 재귀를 이용하여 모든 케이스 찾기

def com(a, b, c, d, e):
    if sum(c) == a:
        print(c)
        e.append(c[:])
    for i in range(d, len(c)):
        if c[i] != 1:
            c[i] = 1
            # print(c)
            com(a, b, c, i, e)
            c[i] = 0
N, M = map(int, input().split())
lst = [0]*(M)
ans = []
com(N, M, lst, 0, ans)
print(len(ans))
