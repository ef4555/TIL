'''
회문의 갯수 세기
회문의 길이 주어짐
가로 또는 세로로 이어진 회문의 개수만 센다
A,B,C로만 구성되어있다
A또한 길이 1짜리 회문이다.
8x8 평면
'''

import sys
sys.stdin = open('HM.txt')
T = 10
for tc in range(1, T+1):
    N = int(input()) # 회문의 크기
    lst = [] # 가로줄 세로줄 저장할 리스트
    for y in range(8):
        garo = input() # 가로줄 입력받아 저장
        lst.append(garo)
    # print(lst)
    for t in range(8): # 세로줄 하나씩 탐색
        sero = ''
        for j in range(8): # 세로줄 0부터7까지 sero문자열로 저장
            sero += lst[j][t]
        lst.append(sero)
    cnt = 0
    for moon in lst: # 문자열 하나씩 탐색
        for q in range(0, 8-N+1): # 범위 설정 전체 문자열 길이에서 -N하고 +1해줘야함, 다음번 슬라이싱때 또 -1 되니까
                if moon[q:q+N][-1] ==  moon[q:q+N][0]: # N개씩 잘라낸 문자열 중 회문이 되기 위한 최소조건 앞 뒤가 같다는것 탐색
                    if moon[q:q+N] == moon[q:q+N][::-1]: # 앞 뒤가 같으면 뒤집어도 나머지가 같은지 탐색
                        cnt += 1
    print(f'#{tc} {cnt}')
