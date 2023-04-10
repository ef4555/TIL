import sys
sys.stdin = open('sample_input (1).txt')
T = int(input())
for tc in range(1, T+1):
    arr = []
    for i in range(5):
        arr.append(list(input()))
    m_max = 0
    for j in arr:
        if m_max <= len(j):
            m_max = len(j)
    for k in arr:
        while len(k) != m_max:
            k.append('')
    print(f'#{tc}', end=' ')
    for jj in range(m_max):
        for ii in range(5):
            print(arr[ii][jj], end='')
    print()
