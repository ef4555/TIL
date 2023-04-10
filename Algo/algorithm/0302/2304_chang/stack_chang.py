import sys
sys.stdin = open('chang.txt')
N = int(input())
lst = []
# x 좌표순서로 버블정렬
for _ in range(N):
    lst.append(list(map(int, input().split())))
for j in range(len(lst)-1, 0, -1):
    for jj in range(0, j):
        if lst[jj][0] > lst[jj+1][0]:
            lst[jj], lst[jj + 1] = lst[jj + 1], lst[jj]

h_max = [0,0]

# print(lst)

# print(lst)
for l in lst:
    if l[1] >= h_max[1]:
        h_max = l # 최고점 구하기
# print(h_max)

# 최고점 인덱스 추출
cnt = 0 # 최고점 인덱스 추출
for ll in lst:
    if ll == h_max:
        break
    cnt += 1
# print(cnt)

# 최고점보다 왼쪽에 있는 점들 검사
h = lst[0][1]
g = lst[0][0]
m_hap = 0
for i in range(cnt+1):
    if lst[i][1] >= h:
        m_hap += h * (lst[i][0] - g)
        g = lst[i][0]
        h = lst[i][1]
# print(m_hap)

# 리스트 뒤집어서 최고점보다 오른쪽에 있는 점들 검사
lst2 = lst[cnt:][::-1] # 최고점 기준 오른쪽에 있는 점들
# print(lst2)
h = lst2[0][1]
g = lst2[0][0]
for i in range(len(lst2)):
    if lst2[i][1] >= h:
        m_hap += h * ((g+1) - (lst2[i][0]+1))
        g = lst2[i][0]
        h = lst2[i][1]

m_hap += h_max[1] # 기둥 넒이 추가
print(m_hap)

