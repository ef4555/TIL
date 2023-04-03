import sys
sys.stdin = open('s_input.txt')
'''
def f(x):
    for j in range(x):
        if row[x] == row[j]:
            return False
    return True
'''

     
 
def choice(x, s):
    global m_v
     
    if x == N:
        if m_v > s:
            m_v = s
        return
 
    if s > m_v:
        return
 
    for i in range(N): # 검사해야할게 열 뿐이라면 검증 함수를 안써도 됨
        if row[i] == 0:
            row[i] = 1
            choice(x+1, s+arr[x][i])
            row[i] = 0


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    m_v = 15*99
    arr = [list(map(int, input().split())) for _ in range(N)]
    # print(arr)
    row = [0]*N
    # print(row)
    choice(0, 0)
    print(f'#{tc} {m_v}')
