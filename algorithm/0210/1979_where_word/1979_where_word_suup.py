import sys
sys.stdin = open('where_word.txt')

def count(arr):
    ans = 0
    for lst in arr:
        cnt = 0
        for n in lst:
            if n == 1: 
                cnt += 1
            else: # 칸 없음
                if cnt == K:
                    ans += 1
                cnt = 0
    return ans 

T = int(input())
for tc in range(1, T+1):
    N, K = map(int,input().split()) 
    arr = [list(map(int, input().split())) + [0] for _ in range(N)] + [[0]*(N+1)]# 가로 줄 한 줄씩 받아서 뒤에 0 추가한다.
    print(arr)
    arr_t = list(map(list, zip(*arr)))
    ans = count(arr) + count(arr_t)

    print(f'#{tc}, {ans}')