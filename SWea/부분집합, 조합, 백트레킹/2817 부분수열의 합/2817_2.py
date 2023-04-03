# SWEA 부분수열의 합
import sys
sys.stdin = open('input.txt')


def c(x, s): # st는 시작지점 x는 카운트 s는 합
    global cnt
    if x == N:
        if s == K:
            cnt += 1
            # print(visited)
        return

    
    c(x+1, s+lst[x])
    c(x+1, s)

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split()) # N은 수열의 크기, K는 목표값
    lst = list(map(int,input().split()))
    visited = [0]*N
    cnt = 0
    c(0, 0)
    print(f'#{tc} {cnt}')