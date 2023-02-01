import sys


sys.stdin = open('joong2.txt')

T = int(input()) 
for c in range(1, T+1):
    t = int(input())
    lst = []
    for v in range(1, t+1):
        a = sys.stdin.readline().split()
        lst.append(a)
    # print(lst)
    result = [[0]*t for aaa in range(t)] 
    
    
    # print(result)
    # 90도 회전 
    def rotation(lt):
        result = [[0]*t for aaa in range(t)]
        ro=[]
        for i in range(t):
            for j in range(t):
                result[j][t-i-1] = lt[i][j]
        for rr in range(t):
            ro.append(result[rr])
        return ro

    print(rotation(lst))
    print(rotation(rotation(lst)))
    print(rotation(rotation(rotation(lst))))
