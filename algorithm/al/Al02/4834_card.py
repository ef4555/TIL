import sys

sys.stdin = open('card.txt')

T = int(input())
for uu in range(1, T+1):
    t = int(input())
    num = int(input())

    con = [0]*(10)
    con_sol = [0]*t
    for i in range(t):
        con[num % 10] += 1
        num //= 10
    max_num = 0
    for j in con:
        if max_num < j:
            max_num = j
    idx = 0
    for k in range(len(con)):
        if max_num == con[k]:
            idx = k


    print(f'#{uu} {idx} {max_num}')


