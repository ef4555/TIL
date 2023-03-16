moon1 = input()
moon2 = moon1.lower()
dic = {}
for i in moon2:
    dic[i] = 0

for j in moon2:
    dic[j] += 1

a = max(dic.values())
lst = []
for k in dic:
    if dic[k] == a:
        lst.append(k)
if len(lst) != 1:
    print('?')
else:
    print(lst[0].upper())