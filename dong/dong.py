import sys
sys.stdin = open('input.txt')
def f(x):
    for j in range(x):
        if row[x] == row[j]:
            return False
    return True
    

def choice(x):
    global m_v
    if x == N:
        print(row)
        result = 1
        for k in range(len(row)):
            # print(arr[k][row[k]]/100)
            result *= arr[k][row[k]]/100 
            print(result)
            if m_v <= result*100:
                m_v = result*100
            # print(m_v)
        
        return 
    else:
        for i in range(N):
            row[x] = i
            if f(x):
                choice(x+1)
                
                
T = int(input())
for tc in range(1, T+1):
    m_v = 0
    N = int(input())
    row = [0]*N
    arr = [list(map(int, input().split())) for _ in range(N)]
    choice(0)