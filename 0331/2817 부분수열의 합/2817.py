# SWEA 부분수열의 합
import sys
sys.stdin = open('input.txt')


def c(st, x, s): # st는 시작지점 x는 카운트 s는 합
    global cnt
    if s == K:
        cnt += 1
        # print(visited)
        return
    if s > K:
        return
    
    for i in range(st, N):
        if visited[i] != 1:
            visited[i] = 1
            c(i, x+1, s+lst[i])
            visited[i] = 0

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split()) # N은 수열의 크기, K는 목표값
    lst = list(map(int,input().split()))
    visited = [0]*N
    cnt = 0
    c(0, 0, 0)
    print(f'#{tc} {cnt}')