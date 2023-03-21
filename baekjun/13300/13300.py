N, K = map(int, input().split())

dic_0={} # 여자방
dic_1={} # 남자방
for l in range(1, 7):
    dic_0[l]=0
    dic_1[l]=0
# print(dic_0) # {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
# print(dic_1) # {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}

for _ in range(N):
    S, Y = map(int, input().split())
    # 여:0 남:1
    if S == 0:
        dic_0[Y] += 1
    else:
        dic_1[Y] += 1


# for p in range()
cnt = 0
for i in range(1, 7):
    if dic_0[i] == 0:
        continue
    elif dic_0[i] < K:
        cnt += 1
    elif dic_0[i] == K:
        cnt += 1
    else:
        if dic_0[i]%K ==0:
            cnt += dic_0[i]//K
        else: 
            cnt += dic_0[i]//K + 1

for j in range(1, 7):
    if dic_1[j] == 0:
        continue
    elif dic_1[j] < K:
        cnt += 1
    elif dic_1[j] == K:
        cnt += 1
    else:
        if dic_1[j]%K ==0:
            cnt += dic_1[j]//K
        else: 
            cnt += dic_1[j]//K + 1
print(cnt)


