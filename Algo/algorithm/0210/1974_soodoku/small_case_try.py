



l = [
8, 4, 5, 2, 9, 6, 1, 3, 7,
1, 3, 6, 7, 5, 8, 4, 9, 2,
9, 7, 2, 1, 3, 4, 6, 5, 8,
2, 9, 7, 4, 6, 3, 8, 5, 1,
4, 6, 1, 5, 8, 2, 9, 7, 3,
5, 8, 3, 9, 7, 1, 2, 4, 6,
3, 2, 8, 6, 4, 5, 7, 1, 9,
7, 1, 4, 3, 2, 9, 6, 8, 5,
6, 5, 9, 8, 1, 7, 3, 2, 4,
4, 5, 7, 1, 6, 3, 8, 2, 9,
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
    # print(nemo)
    if len(nemo) != len(set(nemo)):
        print('네모 틀림')

    nemo = []  
    for i in range(3*v,3*v+3):
        nemo.extend(l[9*i+6:9*i+3+6])
    # print(nemo)
    if len(nemo) != len(set(nemo)):
        print('네모 틀림')    
