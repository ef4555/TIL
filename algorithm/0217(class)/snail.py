''' 입력
3
4
5
6
'''

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = [[0] * N for _ in range(N)]

    i = j = dr = 0  # 초기값 설정
    for cnt in range(1, N * N + 1):
        arr[i][j] = cnt  # 현재좌표에 숫자 기록
        ni, nj = i + di[dr], j + dj[dr]  # 이동할 위치 계산

        # 이동할 위치가 범위내 and 빈칸(==0)인경우 이동
        if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == 0:
            i, j = ni, nj
        else:  # 방향을 꺽어서 이동위치 다시 계산
            dr = (dr + 1) % 4  # 0-1-2-3-1-2..
            i, j = i + di[dr], j + dj[dr]

    print(f'#{test_case}')
    for lst in arr:
        print(*lst)
