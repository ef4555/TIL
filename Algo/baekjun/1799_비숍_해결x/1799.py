# 비숍
import sys
sys.stdin = open("input.txt")




def f(x, i):
    for j in range(x):
        for k in range(N):
            if arr[j][k] == 2:
                if abs(x-j) == abs(i-k): # 대각선에 있으면
                    return False
    return True


def choice(x):
    # print(row)
    global cnt 
    if x == N:
        return
    else:
        for i in range(N):
            if arr[x][i] != 0:
                if f(x, i) : # 대각선을 검증해야함
                    arr[x][i] = 2
                    cnt += 1
        choice(x+1)


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
# print(arr)
cnt = 0
row = [[0]*N for _ in range(N)]
choice(0)
print(cnt)
print(arr)