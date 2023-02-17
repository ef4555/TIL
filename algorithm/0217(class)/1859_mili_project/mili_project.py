'''
직관적인 방법
최대값을 찾으면(i부터 끝까지)
i부터 i_max까지 차이 누적
시작을 i_max +1로 옮겨서 다시 최댓값 찾기
for 문보다 while문이 적합할수 있겠구나 추측
while i < N인경우 반복


뒤부터 생각해보는 방법
기준값을 뒤에서부터 정하면
자기보다 작은 값은 다 내가 최대값이다.
작은값 -> 차이
큰 값 -> 최댓값 갱신(기준값 갱신)
ans = max = 0
for n in lst[::-1]:
 if max > n:
 else: ans += max-n
 max = n


'''



import sys
sys.stdin = open('mili.txt')
T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    lst = list(map(int, input().split()))[::-1]

    ans = mx = 0
    for n in lst:
        if mx > n:
            ans += mx - n
        else:
            mx = n

    print(f'#{test_case} {ans}')



'''
# 직관적인 방법이지만 시간이 오래 걸린다.
    N = int(input())
    lst = list(map(int, input().split()))
    ans = 0
    i = 0
    while i < N:
        # i 부터 끝까지 최대값의 index찾기
        i_max = i
        for j in range(i+1, N):
            if lst[i_max] < lst[j]:
                i_max = j
        # i부터 i_max 까지의 최대값과의 차이 누적
        for j in range(i, i_max):
            ans += lst[i_max] - lst[j]
        i = i_max + 1
    print(f'#{tc} {ans}')
'''