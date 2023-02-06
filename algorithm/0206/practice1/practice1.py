'''
연습문제 1
5x5 2차 배열에 무작위로 25개의 숫자로 초기화 한 후
25개의 각 요소에 대해서 그 요소와 이웃한 요소와의 차의 절댓값을 구하시오
예를 들어 아래 그림에서 7 값의 이웃한 값은 2, 6, 8, 12 이며 차의 절댓값의 합은 12이다
25개의 요소에 대해서 모두 조사하여 총합을 구하시오
벽에 있는 요소는 이웃한 요소가 없을 수도 있다.
'''
import sys
sys.stdin = open('practice1.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [[0] * N for i in range(N)] # d
    for g in range(N):
        arr[g] = list(map(int, input().split()))
    hap = []
    di = [-1, 0, 1, 0]
    dj = [0, 1, 0, -1]
    for i in range(N):
        for j in range(N):
            for k in range(4):
                ni, nj = i+di[k], j+dj[k]
                if 0 <= ni < N and 0 <= nj < N:
                    hap.append(abs(arr[ni][nj]-arr[i][j]))
    print(f'#{tc} {sum(hap)}')


