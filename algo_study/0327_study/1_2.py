# 큰 수의 법칙
N, M, K = map(int, input())
lst = list(map(int, input().split()))
lst.sort()
fst = lst[-1] # 첫 번째로 큰 수
snd = lst[-2] # 두 번째로 큰 수
# M 번 더함
# K 번 연속으로 가능
ans = 0
while True: # break 나올때까지 반복
    for i in range(K):
        if M == 0: # 빼가면서 M 횟수 남았는지 확인
            break
        ans += fst # k번 더하고
        M -= 1
    # k번 더한 후에 M 횟수 남았는지 확인
    if  M == 0:
        break
    ans += snd # 작은것 1번 더하기
    M -= 1
print(ans)

