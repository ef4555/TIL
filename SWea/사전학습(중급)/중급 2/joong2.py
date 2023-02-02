import sys


sys.stdin = open('joong2.txt')

T = int(input())
count = 0
for c in range(1, T+1):
    t = int(input())
    lst = []
    for v in range(1, t+1):
        a = list(map(str, input().split()))
        lst.append(a)
    result = [[0]*t for aaa in range(t)] 
    
    
    # print(result)
    # 90도 회전 
    def rotation(lt):
        result = [[0]*t for aaa in range(t)]
        for i in range(t):
            for j in range(t):
                result[j][t-i-1] = lt[i][j]
        return result
    count += 1
    print(f'#{count}')
    for oo in range(0,t):
        print(''.join(rotation(lst)[oo]), ''.join(rotation(rotation(lst))[oo]), ''.join(rotation(rotation(rotation(lst)))[oo]))
