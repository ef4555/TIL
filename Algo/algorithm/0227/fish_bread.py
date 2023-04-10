import sys
sys.stdin = open('1111.txt')
T = int(input())
for tc in range(1, T+1):
    N, M, K = map(int, input().split()) # N명의 사람들 M초의 시간이 걸려 K개 생산 가능
    lst = list(map(int, input().split()))
    b = -K
    j = 0
    lst.sort()
    print(lst)
    for i in range(0, N):
        while j <= N:
            if i % M == 0:
                b += K
                i += 1
                break
            elif i == lst[j]:
                b -= 1
                j += 1
                if b <= 0:
                    print('false')
                i += 1
                break

            i += 1


