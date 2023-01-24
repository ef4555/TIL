a = int(input())
b = int(input())
value = 0
for i in range(1, b+1):
    c, d = map(int, input().split())
    value += c*d
if a == value:
    print('Yes')
else:
    print('No')

    
   