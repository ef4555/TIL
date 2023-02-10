
'''
N x N 행렬이 주어질 때,

시계 방향으로 90도, 180도, 270도 회전한 모양을 출력하라.


[제약 사항]

N은 3 이상 7 이하이다.

[입력]

가장 첫 줄에는 테스트 케이스의 개수 T가 주어지고, 그 아래로 각 테스트 케이스가 주어진다.

각 테스트 케이스의 첫 번째 줄에 N이 주어지고,

다음 N 줄에는 N x N 행렬이 주어진다.

[출력]

출력의 첫 줄은 '#t'로 시작하고,

다음 N줄에 걸쳐서 90도, 180도, 270도 회전한 모양을 출력한다.

입력과는 달리 출력에서는 회전한 모양 사이에만 공백이 존재함에 유의하라.

(t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)
'''
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
