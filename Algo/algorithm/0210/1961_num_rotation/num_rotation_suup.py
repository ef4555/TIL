# 목적지 기준으로 원본의 어떤 좌표의 값이 저장되는지 확인
# 목적지 기준 i, j 범위를 기준으로 정리
'''
arr1[i][j] = arr[N-j-1][i]
arr2[i][j] = arr[N-j-i][N-1-j]
arr3[i][j] = arr[j][N-1-i]
'''

import sys


sys.stdin = open('joong2.txt', 'r')

T = int(input())
count = 0
for c in range(1, T+1):
    N = int(input())
    arr = [input().split() for _ in range(N)]
    a1 = [[0]*N for _ in range(N)] # 90도
    a2 = [[0]*N for _ in range(N)]
    a3 = [[0]*N for _ in range(N)]

    # 회전각도에 따른 위치값을 저장
    for i in range(N):
        for j in range(N):
            a1[i][j] = arr[N-1-j][i]
            a2[i][j] = arr[N-1-j][N-1-j]
            a3[i][j] = arr[j][N-1-i]


    print(f'#{tc}')
    for a,b,c in zip(a1,a2,a3):
        print(f'{"".join(a)} {"".join(b)} {"".join(c)}')
