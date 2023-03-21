def com(a, b, c, d, e):
    if sum(c) == a:
        print(c)
        d = c
        ans.append(d)
        return
    for i in range(d, len(c)):
        if c[i] != 1:
            c[i] = 1
            # print(c)
            com(a, b, c, d+i, e)
            c[i] = 0
N, M = map(int, input().split())
lst = [0]*(M)
ans = []
com(N, M, lst, 0, ans)
print(ans)
