def sq(a, b):
    global memo
    if b >= 2 and memo[b] == 0:
        memo[b] = a * sq(a, b-1)
    return memo[b]
# memoization 활용
# 중복되는 호출이 없어서 차이 없다.

import sys
sys.stdin = open('je.txt')
# N,M이 주어질 때, N의 M 제곱값을 구하기
T = 10
for tc in range(1, T+1):
    t = int(input())
    N, M = map(int, input().split())
    memo = [0] * (M+1)
    memo[0] = 1
    memo[1] = N
    sq(N, M)
    print(f'#{t} {memo[-1]}')

'''
# 단순 재귀 풀이
def squr(n, m):
    if m <= 0 :
        return 1
    else: # m이 1 이상이면
        return n * squr(n, m-1)
     
T = 10
for tc in range(1, T+1):
    tcn = int(input())
    N, M = map(int, input().split())
    ans = squr(N, M)
     
    print(f'#{tc} {ans}')
    
'''
