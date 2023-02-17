'''
직관적인 방법
구간에서 최대값을 찾고
수익을 내고(최대값이랑 빼야 수익이 최대니까)
그 다음 구간부터 최대값 구하고 수익 내고
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
for tc in range(1, T + 1):
    N = int(input())
    lst = list(map(int, input().split()))
    i = 0
    ans = 0

    while i < N:
        # i부터 끝까지 최대값의 인덱스 찾기
        i_max = i # 최대값을 i로 설정
        for j in range(i + 1, N): # i 다음값부터 끝까지
            if lst[i_max] < lst[j]: # i번째 인덱스 값보다 큰 게 있으면
                i_max = j # 최대값 가리키는 인덱스 변경
        # i부터 i_max 까지의 최대값과의 차이 누적
        for j in range(i, i_max): # i부터 찾은 최대값-1 인덱스까지
            ans += lst[i_max] - lst[j] # i_max값과의 차이를 더한다
        i = i_max + 1 # 인덱스 위치 최댓값 +1로 변경
    print(f'#{tc} {ans}')

'''
import sys
sys.stdin = open('mili.txt')
T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    lst = list(map(int, input().split()))[::-1] # 거꾸로 탐색한다

    ans = mx = 0 # 답이랑 최대값이랑 0으로 놓고
    for n in lst: # lst에서 최소값 훝으면서
        if mx > n: 
            ans += mx - n
        else:
            mx = n

    print(f'#{test_case} {ans}')

'''