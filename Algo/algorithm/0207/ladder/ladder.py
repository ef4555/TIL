import sys
sys.stdin = open('ladder.txt')

T = 10
for tc in range(1, T+1):
    N = int(input())
    ladder = [[0]*100 for _ in range(100)]
    for i in range(100):
        l = list(map(int, input().split()))
        ladder[i] = l
    a = 0
    b = 0
    for i in range(100):
        for j in range(100):
            if ladder[i][j] == 2:
                a, b = i, j

    dj = [1, -1] # 우 좌 방향
    while a > 0:
        if b == 0: # 왼쪽 끝인 경우
            nr = b + dj[0]
            nl = b + dj[1]

            if 0 <= a < 100 and 0 <= nr < 100:
                if ladder[a][nr] == 0:
                    a -= 1
                elif ladder[a][nr] == 1:
                    b += 1
                    while ladder[a - 1][b] == 0 and ladder[a + 1][b] == 0:
                        b += 1
                    a -= 1
        elif b == 99: # 오른쪽 끝인 경우
            nr = b + dj[0]
            nl = b + dj[1]

            if 0 <= a < 100 and 0 <= nl < 100:
                if ladder[a][nl] == 0:
                    a -= 1
                elif ladder[a][nl] == 1:
                    b -= 1
                    while ladder[a - 1][b] == 0 and ladder[a + 1][b] == 0:
                        b -= 1
                    a -= 1

        else:
            nr = b + dj[0]
            nl = b + dj[1]

            if 0 <= a < 100 and 0 <= nr < 100 and 0 <= nl < 100:
                if ladder[a][nr] == 0 and ladder[a][nl] == 0:
                    a -= 1
                elif ladder[a][nl] == 1:
                    b -= 1
                    while ladder[a - 1][b] == 0 and ladder[a + 1][b] == 0:
                        b -= 1
                    a -= 1
                elif ladder[a][nr] == 1:
                    b += 1
                    while ladder[a - 1][b] == 0 and ladder[a + 1][b] == 0:
                        b += 1
                    a -= 1

    print(f'#{tc} {b}')








