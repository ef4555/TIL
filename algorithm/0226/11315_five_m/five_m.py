import sys
sys.stdin = open('sample_input.txt')
T = int(input())
for tc in range(1, T+1):
    N = int(input()) # 판 크기
    arr = [list(input()) for _ in range(N)]
    # print(arr)
    ans = 'NO'
    d = ((-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)) # 8방향 설정
    for i in range(N):
        for j in range(N):
            cnt = 0
            if arr[i][j] == 'o':
                for k in range(8):
                    for mul in range(1, 5):
                        ni = i + mul*d[k][1]
                        nj = j + mul*d[k][0]
                        if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == 'o':
                            cnt += 1
                            if cnt == 4:
                                ans = 'YES'
                        else:
                            cnt = 0
                            break

    print(f'#{tc} {ans}')

