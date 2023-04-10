N = int(input())
M = list(map(int, input().split()))
M.sort()
a = M[-1]
ans = 0
for k in M:
    ans += k/a*100
print(ans/len(M))
