# 숫자 카드 게임
# 행마다 가장 작은 수를 찾은 뒤에 그 수 중에서 가장 큰 수를 찾는다.
N, M =map(int,input().split())
ans = 0
for i in range(N):
    lst = list(map(int,  input().split()))
    min_v = min(lst)
    ans = max(ans, min_v)
print(ans)