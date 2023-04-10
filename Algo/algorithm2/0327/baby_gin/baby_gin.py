def perm(i, k):
    global ans
    if i == k:
        # print(p)
        if p[0]+1 == p[1] and p[1]+1 == p[2] and p[3] == p[4] == p[5]:
            ans = True
            return
        elif p[0] == p[1] == p[2] and p[3] == p[4] == p[5]:
            ans = True
            return
    else:
        for j in range(0, k):  # 사용하지 않은 숫자를
            if used[j] == 0:  # used에서 순서대로 검색
                p[i] = lst[j]
                used[j] = 1  # j번 자리 숫자 사용으로 표시
                perm(i + 1, k) # 사용한 숫자 빼고 검색
                used[j] = 0  # j번 자리 숫자를 다른 자리에서 쓸 수 있게



N = int(input())
for _ in range(N):
    ans = False
    lst = list(map(int, input()))
    p = [0] * len(lst)
    used = [0] * len(lst)
    perm(0, len(lst))
    print(ans)