'''
3
3 6
5 15
5 10
'''


import sys

sys.stdin = open('booboon_set_hap.txt')
T = int(input())
A = [ a for a in range(1, 13)]
for tc in range(1, T+1):
    cnt = 0
    N, K = map(int, input().split())
    for i in range(1<<12):
        hap = []
        for j in range(12):
            if i & (1<<j):
                hap.append(A[j])
        if len(hap) == N and sum(hap) == K:
            cnt += 1
    print(f'#{tc} {cnt}')




