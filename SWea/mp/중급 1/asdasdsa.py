



l = [
7, 3, 6, 4, 2, 9, 5, 8, 1,
5, 8, 9, 1, 6, 7, 3, 2, 4, 
2, 1, 4, 5, 8, 3, 6, 9, 7, 
8, 4, 7, 9, 3, 6, 1, 5, 2, 
1, 5, 3, 8, 4, 2, 9, 7, 6, 
9, 6, 2, 7, 5, 1, 8, 4, 3, 
4, 2, 1, 3, 9, 8, 7, 6, 5, 
3, 9, 5, 6, 7, 4, 2, 1, 8, 
6, 7, 8, 2, 1, 5, 4, 3, 9
]

for v in range(0,3):
    nemo = []
    for i in range(3*v,3*v+3):
        nemo.extend(l[9*i:9*i+3])
    print(nemo)
    if len(nemo) != len(set(nemo)):
        print('네모 틀림')

    nemo = []
    for i in range(3*v,3*v+3):
        nemo.extend(l[9*i+3:9*i+3+3])
    print(nemo)
    if len(nemo) != len(set(nemo)):
        print('네모 틀림')

    nemo = []  
    for i in range(3*v,3*v+3):
        nemo.extend(l[9*i+6:9*i+3+6])
    print(nemo)
    if len(nemo) != len(set(nemo)):
        print('네모 틀림')    
