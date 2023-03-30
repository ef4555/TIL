import sys
sys.stdin = open('input.txt')
def f(x):
    for j in range(x):
        if row[x] == row[j]:
            return False
    return True
    

def choice(x, r):
    global m_v
    # if r*100 <= m_v:
    #     return
    
    if x == N:
        # r *= arr[x][row[x]]/100
        # for l in range(N):
        #     r *= arr[l][row[l]]/100
        if m_v <= r*100:
            m_v = r*100
            # print(row)
            # print(m_v)
        return 



    for i in range(N):
        row[x] = i
        if arr[x][row[x]] == 0:
            continue
        if f(x):
            # r*=arr[x][i]/100
            choice(x+1, r*arr[x][i]/100)
                
                
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    row = [0]*N
    cnt = 1  
    # for i in range(N):  # 행
    #     temp = 0
    #     for j in range(N):  # 열
    #         if not row[j]:
    #             if temp < arr[i][j]:
    #                 temp = arr[i][j]
    #                 idx = j
    #     cnt *= temp
    #     row[idx] = 1
    # m_v = cnt
    m_v = 0
    print(cnt)
    row = [0]*N
    choice(0, 1)
    print("#{} {:.6f}".format(tc, m_v))