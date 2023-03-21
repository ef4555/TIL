N = int(input())
c = 1
while c <= N:
    dic = {}
    for k in range(1, 5):
        dic[k] = 0
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    for i in range(1, len(a)):
        dic[a[i]] += 1
    # print(dic)
    for j in range(1, len(b)):
        dic[b[j]] -= 1  
    cnt = 0
    ii = 4
    # print(dic)
    while True:
        if ii == 0:
            print('D')
            break
        elif dic[ii] > 0:
            print('A')
            break
        elif dic[ii] <0:
            print('B')
            break
        else:
            ii -= 1
            continue
    c += 1