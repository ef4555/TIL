import sys
sys.stdin = open('godae.txt')


def count(arr):
    mx = 2
    for lst in arr:
        cnt = 0
        for n in lst:
            if n == 1:
                cnt += 1
                if mx < cnt:
                    mx = cnt
            else:
                cnt = 0
    return mx






T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)] # 가로줄 저장
    arr_t = list(map(list,zip(*arr))) # 세로줄 저장


    ans = count(arr) # 가로줄 최대값 찾기
    t = count(arr_t) # 세로줄 최대값 찾기
    if ans < t: # 가로 세로 최대값 비교
        ans = t
    print(f'#{tc} {ans}')