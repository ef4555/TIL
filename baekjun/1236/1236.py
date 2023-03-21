N, M = map(int, input().split())
arr = [input() for _ in range(N)]
arr2 = ['' for _ in range(M)]
for i in range(M):
    for j in range(N):
        arr2[i] += arr[j][i]
print(arr2)
cnt2 = M
for kk in arr2:
    if 'X' in kk:
        cnt2 -= 1
print(arr)
cnt1 = N
for ll in arr:
    if 'X' in ll:
        cnt1 -= 1

print(max(cnt1, cnt2))
