A, B = map(int,input().split())
i = B
j = 1
lst = [0]

while len(lst) <= i:
    for kk in range(j):
        lst.append(j)
    j += 1

print(sum(lst[A:B+1]))