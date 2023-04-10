N = int(input())
lst = []
for i in range(1, N+1):
    lst.append(i)
while len(lst) > 1:
    aa = lst.pop(0)
    print(aa, end=' ')
    a = lst.pop(0)
    lst.append(a)
print(*lst)
