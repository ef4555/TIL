lst =[]
for _ in range(9):
    a = int(input())
    lst.append(a)


m = max(lst) # 최댓값 저장
lst2 = list(enumerate(lst))
for i in range(len(lst)):
    if m == lst2[i][1]:
        print(lst2[i][1])
        print(lst2[i][0]+1)

