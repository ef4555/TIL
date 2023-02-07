'''
달팽이는 1부터 N*N까지의 숫자가 시계방향으로 이루어져 있다.

다음과 같이 정수 N을 입력 받아 N크기의 달팽이를 출력하시오.

'''
import sys
sys.stdin = open('snail.txt')
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    F = [[0]*N for _ in range(N)]
    a = 0
    b = 0
    num = 1
    di = [0, 1, 0, -1] # 하상
    dj = [1, 0, -1, 0] # 우좌
    for y in range(N):
        F[a][y] = num
        num += 1

    print(F)











