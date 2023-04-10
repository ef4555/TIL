import sys
sys.stdin = open('sample_input.txt')
T = int(input())
for tc in range(1, T+1):
    N, M = map(str, input().split())
    K = bin(int(M, 16))
    anw = K[2::]
    while int(N) * 4 > len(anw):
        anw = '0' + anw
    print(f'#{tc} {anw}')