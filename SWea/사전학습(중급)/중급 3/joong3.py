import sys

sys.stdin = open('input.txt')
count = 0
T = int(input())
for uu in range(1, T+1):
    n, m = map(int, input().split())
    a_list = list(map(int, input().split()))
    b_list = list(map(int, input().split()))
    print(a_list)
    print(b_list)
    max_lst = []
    a = 0
    b = 0
    if m > n:
        a = m
        b = n
    else:
        a = n
        b = m

    for k in range(0,a-b+1):
        lst = []
        for i in range(0,b):
            hap = 0
            if len(a_list) < len(b_list):
                hap += a_list[i]*b_list[i+k]
                lst.append(hap)
            else:
                hap += b_list[i]*a_list[i+k]
                lst.append(hap)
        max_lst.append(sum(lst))
    count += 1
    print(f'#{count} {max(max_lst)}')



