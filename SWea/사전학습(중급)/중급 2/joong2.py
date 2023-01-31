import sys


sys.stdin = open('joong2.txt')

T = int(input()) 
for c in range(1, T+1):
    t = int(input())
    a_lst = [] 
    for v in range(1, t+1):
        a = sys.stdin.readline().split()
        for num in a:
            a_lst.append(num)
    print(a_lst)
    num_1 = ''
    for y in range(t-1, -1, -1):
        num_1 += a_lst[y*t]
    num_2 = ''.join(a_lst[-1:-(t+1):-1])
    num_3 = ''
    for y in range(1, t+1):
        num_3 += a_lst[3*y-1]    

    num_4 = ''
    for y in range(t-1, -1, -1):
        num_4 += a_lst[y*t+1]
    num_5 = ''.join(a_lst[-4:-(t+4):-1])
    num_6 = ''
    for y in range(1, t+1):
        num_6 += a_lst[3*y-2]

    num_7 = ''
    for y in range(t-1, -1, -1):
        num_7 += a_lst[y*t+2]
    num_8 = ''.join(a_lst[-7:-(t+7):-1])
    num_9 = ''
    for y in range(1, t+1):
        num_9 += a_lst[3*y-3]        
    print(num_1, num_2, num_3)    
    print(num_4, num_5, num_6)
    print(num_7, num_8, num_9)





        
