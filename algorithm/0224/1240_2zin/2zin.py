import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(input()[::-1]) for _ in range(N)]
    # print(arr)
    moon = ''
    k = 0
    while k == 0:
        for i in range(N):
            for j in range(M):
                if arr[i][j] == '1':
                    moon += ''.join(arr[i][j:j+56][::-1])
                    k = 1
                    break
    m = moon[0:56]
    # print(m)
    l = 0
    am = []
    while l <= 7:
        a = m[7*l:7*l+7]
        if a == '0001101':
            am.append(0)
        elif a == '0011001':
            am.append(1)
        elif a == '0010011':
            am.append(2)
        elif a == '0111101':
            am.append(3)
        elif a == '0100011':
            am.append(4)
        elif a == '0110001':
            am.append(5)
        elif a == '0101111':
            am.append(6)
        elif a == '0111011':
            am.append(7)
        elif a == '0110111':
            am.append(8)
        elif a == '0001011':
            am.append(9)
        l += 1
    # print(am)
    ll = 0
    even = 0
    odd = 0
    while ll <= 3:
        odd += am[2*ll]
        even += am[2*ll+1]
        ll += 1
    # print(odd)
    # print(even)
    if (odd * 3 + even) % 10 == 0:
        print(f'#{tc} {(odd + even)}')
    else:
        print(f'#{tc} 0')
