import sys
sys.stdin = open('input.txt')

def find_set(x): # x가 속한 집합의 대표원소 리턴
    while x != rep[x]: # x == rep[x]가 될때까지
        x = rep[x] 
    return x        
    
def union(x, y): # y의 대표원소가 x의 대표원소를 가리키도록 함
    rep[find_set(y)] = find_set(x)

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    rep = [i for i in range(N+1)] 
    lst = list(map(int, input().split()))
    
    for i in range(0,len(lst),2):
        union(lst[i],lst[i+1])
        
    result = set()
    
    for i in range(1, N + 1):
        print(find_set(i))
        result.add(find_set(i))
    print(result)
        
    print(f'#{tc} {len(result)}')
    


