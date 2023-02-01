import sys

sys.stdin = open('input.txt')
T = 10
for tt in range(1, T+1):
    count = int(input())
    num_lst = []
    big_lst = [0 for i in range(100)] # 배열을 저장할 빈 리스트
    for dd in range(0, 100):
        lst = list(map(int, input().split()))
        big_lst[dd] = lst
    sero = [0 for i in range(100)]
    # 가로 합
    for nn in range(100):
        num_lst.append(sum(big_lst[nn]))

        for tt in range(100):
            sero[tt] = big_lst[tt][nn]
    print(sero)
    # 세로 합
    # for kk in range(100):
        # num_lst.append(sum(sero[nn]))

    # 대각선 합
    dae1 = [0 for i in range(100)]
    dae2 = [0 for i in range(100)]
    for yy in range(100):
        big_lst[yy][yy] = dae1[yy]
    for ii in range(100):
        big_lst[99-ii][ii-1] = dae1[ii]

    num_lst.extend(dae1)
    num_lst.extend(dae2)
    # print(num_lst)








