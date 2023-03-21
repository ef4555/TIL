N, k = map(int, input().split())

dic_0={} # 여자방
dic_1={} # 남자방
for l in range(1, 7):
    dic_0[l]=0
    dic_1[l]=0
print(dic_0) # {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
print(dic_1) # {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}

for _ in range(N):
    S, Y = map(int, input().split())
    # 여:0 남:1
    if S == 0:
        dic_0[Y] += 1
    else:
        dic_1[Y] += 1


# for p in range()
print(dic_0)
print(dic_1) 

