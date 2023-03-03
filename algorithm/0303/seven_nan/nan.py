
import sys
sys.stdin = open('nan.txt')
lst = []
for _ in range(9):
    lst.append(int(input()))
hap = sum(lst)
for j in range(8):
  for k in range(j+1, 9):
    if hap - (lst[j] + lst[k]) == 100:
      fake1 = lst[j]
      fake2 = lst[k]
      break

lst.remove(fake1)
lst.remove(fake2)
lst.sort()
for i in lst:
  print(i)