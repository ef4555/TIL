import sys
sys.stdin = open('111.txt')

N, M = map(int, input().split()) # N개의 달걀, M명의 고객
lst = [int(input()) for _ in range(M)]
lst.sort()
print(lst)
m_cnt = 0
for i in range(lst[-1]+1):
    cnt = 0
    for j in lst:
        if i <= j:
            cnt += i
    if m_cnt <= cnt:
        m_cnt = cnt


print(cnt)