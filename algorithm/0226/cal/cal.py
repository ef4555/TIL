def calc(n):
    if len(tree[n]) == 2:
        return int(tree[n][1])
    else:
        L = calc(int(tree[n][2]))
        R = calc(int(tree[n][3]))

        if tree[n][1] == '+':
            return L + R
        elif tree[n][1] == '-':
            return L - R
        elif tree[n][1] == '*':
            return L * R
        elif tree[n][1] == '/':
            return L / R


for tc in range(1, 11):
    N = int(input())
    tree = [0 for _ in range(N + 1)]
    for _ in range(N):
        tmp = input().split()
        tree[int(tmp[0])] = tmp
    print('#{} {}'.format(tc, int(calc(1))))
