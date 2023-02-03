import sys

sys.stdin = open('sooo.txt')
T = int(input())
for tc in range(1, T+1):
    div = [2, 3, 5, 7, 11]
    N = int(input())
    cnt = [0] * (len(div))
    for i in range(len(div)):
        while N % div[i] == 0:
            N = N / div[i]
            cnt[i] += 1


    print(f'#{tc}', *cnt)