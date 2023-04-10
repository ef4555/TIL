import sys
sys.stdin = open('bin.txt')


def bin_sort(P, K):
    start = 1
    cnt = 0
    end = K
    while start <= end :
        middle = (start+end)//2
        cnt += 1
        if middle == P:
            return cnt
        elif middle > P:
            end = middle
        else:
            start = middle 
    return cnt

T = int(input())
for tc in range(1, T+1):
    e, A, B = map(int, input().split())
    cnt1 = bin_sort(A, e)
    cnt2 = bin_sort(B, e)

    if cnt1 > cnt2:
        print(f'#{tc} B')
    elif cnt1 < cnt2:
        print(f'#{tc} A')
    else:
        print(f'#{tc} 0')

