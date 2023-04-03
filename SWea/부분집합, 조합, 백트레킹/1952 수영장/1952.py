# 수영장
import sys
sys.stdin = open('sample_input (1).txt')



def dfs(n, sm):
    global ans
    if ans<=sm:
        return
    if n > 12:
        ans = min(ans, sm)
        return
    dfs(n+1, sm+day*lst[n]) # 일간권
    dfs(n+1, sm+mon) # 1달권
    dfs(n+3, sm+mon3) # 3달권
    dfs(n+12, sm+year) # 1년권

T = int(input())
for tc in range(1, T+1):
    day, mon, mon3, year = map(int, input().split()) # 각각 이용권의 가격 저장
    lst = [0] + list(map(int, input().split())) # 0부터 12까지 
    
    ans = 365 * 3000
    dfs(1, 0)
    print(f'#{tc} {ans}')
