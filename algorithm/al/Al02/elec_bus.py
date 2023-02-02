import sys

sys.stdin = open('elec_bus.txt')

T = int(input())
for ii in range(1, T+1):
    K, N, M = map(int,input().split())
    lst = list(map(int,input().split()))
    st = 0
    choong = 0
    count = 0
    while st < N:
        a = []
        b = []
        st += K
        for i in lst:
            if i <= st:
                a.append(i)
            else:
                b.append(i)

        print(a)
        print(b)
        count += 1

    print(f'#{ii} {choong}')



