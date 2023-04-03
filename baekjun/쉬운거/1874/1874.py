from collections import deque


n = int(input())
stack = deque([])
ans = []
a  = True
i = 1

for _ in range(n):
    num = int(input())
    while i <= num:      
        stack.append(i)
        ans.append("+")
        i += 1
 

    if stack[-1] == num:    
        stack.pop()        
        ans.append("-")
    else:                   
        print("NO")       
        a = False          
        break               

if a == True:
    for m in ans:
        print(m)