import sys
sys.stdin = open('sample_in1.txt')
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    gi = int(N/2)
    ci = list(map(int, input().split()))
    ci.sort()
    ans = 0
    print(ci)
    minV = 1000
    for i in range(N-2):
        for j in range(i+1, N-1):
            if ci[i] != ci[i+1] and ci[j] != ci[j+1]:
                A = i+1
                B = j-i
                C = N-1-j
                if A*B*C != 0 and A <= N//2 and B <= N//2 and C <= N//2:
                    if minV > max(A, B, C) - min(A, B, C):
                        minV = max(A, B, C) - min(A, B, C)
                    # print(ci[0:i+1], ci[i+1:j+1], ci[j+1:])
    if minV == 1000:
        minV = -1
    print(f'#{tc} {minV}')



