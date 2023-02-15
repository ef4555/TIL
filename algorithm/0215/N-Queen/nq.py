N = 8
lst = [[0] * N for _ in range(N)]
a, b = 1, 1

for j in range(N):
    lst[a][j] = 1
    lst[j][b] = 1
    if 0 <= a+j < N and 0 <= b+j < N:
        lst[a + j][b + j] = 1
        lst[a - j][b - j] = 1
    if 0 <= a - j < N and 0 <= b + j < N:
        lst[a - j][b + j] = 1
    if 0 <= a + j < N and 0 <= b - j < N:
        lst[a + j][b - j] = 1

    j_stack = []
    j_possible = []
    for l in range(N):
        for p in range(N):
            if lst[l][p] == 0:
                j_possible.append([l,p])
    while j_stack:  # 스택에 이동 가능 지점이 있을 때까지


print(stack)
for _ in lst:
    print(_)