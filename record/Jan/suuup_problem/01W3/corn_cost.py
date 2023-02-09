grain_lst = [('고구마',3000), ('감자',2000), ('옥수수',4500),('토란',1300)]

'''
cost = []
for i in grain_lst:
    cost.append(i[1])
cost.sort()
for name in grain_lst:
    if name[1] == cost[-1]:
        print(name[0])
'''

cost = [0, 0]
for i in grain_lst:
    if cost[1] < i[1]:
        cost[0] = i[0]
        cost[1] = i[1]
print(cost[0])
