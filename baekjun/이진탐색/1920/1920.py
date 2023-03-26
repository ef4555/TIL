import sys
input=sys.stdin.readline

def b(l, N, s, e): # 이진 탐색 함수
    if s > e: # 시작점이 끝점보다 크면 
        return 0 # 0을 반환
    m = (s+e)//2 # 중간지점 m
    if l == N[m]: # 찾으려는 수가 중간에 있는 수와 같으면 
        return 1 # 탐색 성공
    elif l < N[m]: # 찾으려는 수가 중간에 있는 수보다 작으면 
        return b(l, N, s, m-1) # 작은 부분 탐색
    else:
        return b(l, N, m+1, e) # 아니면 절반 나눈 것의 큰 부분 탐색
    
n = int(input())
N = sorted(map(int,input().split())) # 크기순으로 정렬
m = int(input())
M = map(int,input().split())

for l in M:
    s = 0
    e = len(N)-1
    print(b(l,N,s,e))