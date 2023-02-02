import sys

sys.stdin = open('input.txt')
T = 10
for tt in range(1, T+1):
    count = int(input())
    num_lst = [] # 합들을 저장할 리스트
    big_lst = [[] for i in range(100)] # 배열을 저장할 빈 리스트
    for dd in range(0, 100):
        lst = list(map(int, input().split()))
        big_lst[dd].extend(lst)
    sero = [[] for pp in range(100)]
    # 가로 합
    for nn in range(0, 100):
        num_lst.append(sum(big_lst[nn]))

        for tt in range(0, 100):
            sero[nn].append(big_lst[tt][nn])
    # 세로 합
    for kk in range(100):
        num_lst.append(sum(sero[kk]))

    # 대각선 합
    dae1 = [0 for i in range(100)]
    dae2 = [0 for i in range(100)]
    for yy in range(100):
        big_lst[yy][yy] = dae1[yy]
    for ii in range(100):
        big_lst[99-ii][ii-1] = dae1[ii]

    num_lst.append(sum(dae1))
    num_lst.append(sum(dae2))
    print(f'#{count} {max(num_lst)}')









