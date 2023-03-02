import sys
sys.stdin = open('chang.txt')
N = int(input())
lst = []
for _ in range(N):
    lst.append(list(map(int, input().split())))
lst.sort()
h_max = [0,0]

# print(lst)
for l in lst:
    if l[1] >= h_max[1]:
        h_max = l # 최고점 구하기
# print(h_max)
cnt = 0 # 최고점 인덱스 추출
for ll in lst:
    if ll == h_max:
        break
    cnt += 1
# print(cnt)


m = lst[0][1] # 높이
kk = lst[0][0] # 좌표
m_hap = 0

# print(kk, m)
for i in range(0, cnt+1):
    if lst[i][1] >= m:
        m_hap += m * (lst[i][0] - kk)
        m = lst[i][1]
        kk = lst[i][0]
lst2 = lst[cnt:][::-1]
# print(lst2)
m = lst2[0][1]
kk = lst2[0][0]
# print(lst)
for i in range(len(lst2)):
    if lst2[i][1] >= m: # 높이가 커지면
        m_hap += m * ((kk+1) - (lst2[i][0]+1))
        m = lst2[i][1]
        kk = lst2[i][0]

m_hap += h_max[1]
print(m_hap)

