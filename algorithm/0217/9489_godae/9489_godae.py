'''
각 구역별로 가장 긴 구조물의 길이를 찾는 프로그램 만드시오

'''

import sys
sys.stdin = open('godae.txt')
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    # N개의 줄에 M개씩 데이터가 제공된다
    arr = [list(map(int, input().split())) for _ in range(N)] # 가로줄 저장
    print(*arr) # arr을 한꺼풀 까준다 리스트만 남도록
    print(list(zip([0,1,0], [0,1,0], [0,1,0])))
    arr_t = list(map(list,zip(*arr))) # 세로줄 저장
    # zip함수는 가로줄 정보를 리스트로 받아서 첫번째끼리 두번째끼리 세번째끼리 튜플로 만들어줌
    # zip은 같은 순번끼리 엮어줌
    # 튜플로 만들어준걸 이용하기 편하게 리스트로 다시 바뀌줌
    print(arr_t)
'''
    cnt_max = 0
    cnt = 0
    for i in range(M):
        sero = []
        for j in range(N):
            sero.append(arr[j][i])
        arr.append(sero)



    for k in range(len(arr)):
        for l in arr[k]:
            if l == 1:
                cnt += 1
                if cnt > cnt_max:
                    cnt_max = cnt
            else:
                cnt = 0
        cnt = 0
    print(f'#{tc} {cnt_max}')
'''

