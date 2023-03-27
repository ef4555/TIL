# 1이 될 때까지
# N에서 1을 뺀다
# N을 K로 나눈다.
# K로 나누는 것이 1을 빼는 과정보다 훨씬 빠르게 1으로 만들 수 있음
# K로 나누어 떨어질 때 까지 1을 빼고 K로 나눈다


N, K = map(int, input().split())
result = 0
while N >= K :
    # N이 K로 나누어지지 않는다면 N에서 1씩 빼기
    while N % K != 0:
        N -= 1
        result += 1
    # K로 나누기
    N//=K
    result += 1
# 마지막으로 남은 수에 대하여 1씩 빼기
while N > 1:
    N -= 1
    result += 1

print(result)