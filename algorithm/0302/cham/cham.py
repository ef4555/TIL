import sys
sys.stdin = open('cham.txt')
N = int(input())
d = ((0,0),(0,1),(0,-1),(1,0),(-1,0))# 동서남북
ii = 0
jj = 0
lst = []
d_lst = []
i_lst = []
j_lst = []


for kk in range(6):
    dr, l = map(int, input().split())
    ni = ii + l*d[dr][1]
    nj = jj + l*d[dr][0]
    lst.append([ni,nj])
    i_lst.append(ni)
    j_lst.append(nj)
    ii = ni
    jj = nj
i_lst.sort()
j_lst.sort()
print(lst)
p_max = 0
q_max = 0
for i in range(len(lst)):
    if lst[i][0] >= p_max:
        p_max = lst[i][0]
    if lst[i][1] >= q_max:
        q_max = lst[i][1]


