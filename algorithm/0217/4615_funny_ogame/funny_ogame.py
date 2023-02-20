'''
초기 모양 배치
사방에 0으로 둘러준다면 범위체크 필요 없음
arr[si][sj] = d
8방향 뻗어나가면서
arr[ni][nj] == 0이면 암것도 안함 break
arr[ni][nj] == 다른돌이면 뒤집을 후보, 리스트에 추가
arr[ni][nj] == 같은 돌이면 리스트에 있는 것들 뒤집기
게임이 끝난 후 흑돌 백돌의 개수 출력

'''


import sys
sys.stdin = open('game.txt')
T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [[0] * (N+2) for _ in range(N+2)] # 0으로 둘러싸줌, 좌표가 인덱스값으로 일치
    mid = N//2 # 중간값, 4면 2, 6이면 3, 8이면 4
    arr[mid][mid] = 2
    arr[mid+1][mid] = 1
    arr[mid][mid+1] = 1
    arr[mid+1][mid+1] = 2
    w = 0
    b = 0
    print(arr)
    # 처음 돌 세팅
    # 1이 흑돌, 2가 백돌
    d = [[-1,-1], [-1,0], [-1,1], [0,1], [0,-1], [1,1], [1,0], [1, -1]] # 시계방향으로 8방향
    for i in range(M): # 돌 정보를 받아서 두는것까지 반복문 안에 구현
        si, sj, c = map(int, input().split())
        # 돌을 놓으면 사방을 탐색하면서 흰 돌이 있는 방향 탐색
        # 다음 검은 돌이 나오는 범위까지 뒤집기
        arr[si][sj] = c
        for j in range(8):
            hoobo = []
            for mul in range(1, N): # 증가하면서 찾아냄
                nj = sj + d[j][0]*mul  # 세로 좌표
                ni = si + d[j][1]*mul  # 가로 좌표
                # if 1 <= ni <= N and 1 <= nj <= N:
                if arr[ni][nj] != c: # 자신의 돌 색깔과 다른 돌 발견하면
                    # 그 방향으로 탐색 계속해서 같은 돌 색깔이 나오면 중지해야함...
                    # 후보 스택에 쌓아놓고 같은 돌 색이 나오면 터트리는 방식
                    hoobo.append((ni, nj))
                else:
                    for kk in hoobo: # 같은 돌 발견하면 스택에서 좌표들 꺼내서
                        arr[kk[0]][kk[1]] = c # 그 동안 있던 돌 뒤집기
                    break # 탐색 끝

    for ii in range(1, N+1): # 흰돌 검은돌 갯수 세기(범위 주의! 1부터 N까지 세어야 한다, arr는 0으로 둘러싸져있음)
        for jj in range(N+1):
            if arr[ii][jj] == 1:
                b += 1
            elif arr[ii][jj] == 2:
                w += 1

    print(arr)
    print(f'#{tc} {b} {w}')




