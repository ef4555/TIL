import sys
sys.stdin = open('crop.txt')
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    batt_garo =[[0]*N for _ in range(N)]
    for y in range(N):
        c = list(input())
        batt_garo[y] = c
    print(batt_garo)
    money = 0
    l = N//2 # N값의 중간값
    for i in range(l):
        print(batt_garo[i][l-i:l+i+1])
    for j in range(l, N):
        print(batt_garo[j][N-j-1:N+j+1])