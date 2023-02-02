import sys

sys.stdin = open('elec_bus.txt')

T = int(input())
for ii in range(1, T+1):
    K, N, M = map(int,input().split())
    lst = list(map(int,input().split()))
    st = 0
    choong = 0

    while st < N:
        a = []
        b = []
        st += K
        for i in lst:
            if i <= st:
                a.append(i)
            else:
                b.append(i)
        if b == []:
            choong += 1
            break
        elif  a[-1]+ K < b[0] :
            choong = 0
            break
        st = a[-1]
        choong += 1
    print(f'#{ii} {choong}')



