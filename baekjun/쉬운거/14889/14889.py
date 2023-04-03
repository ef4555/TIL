from itertools import combinations

N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]

lst = [i for i in range(N)]

m = int(N/2)
# print(lst[:m], lst[m:])
min_v = 100000
aa = list(combinations(lst, m))
for k in aa:
    b = set(lst)
    a = set(k)
    b = list(b-a)
    a = list(a)    
    # print(a, b)
    team1_com = list(combinations(a, 2))
    team2_com = list(combinations(b, 2))
    # print(team1_com, team2_com)
    v1 = 0
    v2 = 0
    for ii in team1_com:
        v1 += arr[ii[0]][ii[1]] 
        v1 += arr[ii[1]][ii[0]] 
    for jj in team2_com:
        v2 += arr[jj[0]][jj[1]] 
        v2 += arr[jj[1]][jj[0]] 
    if abs(v1-v2) <= min_v:
        min_v = abs(v1-v2)
print(min_v)