N = int(input())
for _ in range(N):
    aa = str(input())
    p = 0
    cnt = 0
    for k in aa:
        if k == 'O':
            cnt += 1
            p += cnt
        else:
            cnt = 0
    print(p)
