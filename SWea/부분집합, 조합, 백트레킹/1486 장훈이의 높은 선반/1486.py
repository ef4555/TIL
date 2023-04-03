import sys
sys.stdin = open('2.txt')

def c(st, x, s):
    global m_v
    if s >= B:
        hap = 0
        # print(visited)
        for k in range(N):
            if visited[k] == 1:
                hap += lst[k]
        if hap <= m_v:
            m_v = hap
            
        return
    
    
    
    
    for i in range(st, N):
        if visited[i] != 1:
            visited[i] = 1
            c(i, x+1, s+lst[i])
            visited[i] = 0
            
T = int(input())
for tc in range(1, T+1):
    N, B = map(int, input().split()) # N은 사람의 수, B는 서랍의 높이
    lst = list(map(int, input().split()))
    visited = [0]*N
    m_v = 10000*20
    # 높이가 B 이상인 경우 중 높이가 B에 가장 작게 차이나는 경우
    c(0, 0, 0)
    print(f'#{tc} {abs(B-m_v)}')
    