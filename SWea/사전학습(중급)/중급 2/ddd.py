T = int(input())
count = 0
for i in range(0, T+1):
    count += 1

    N = int(input())
    lst = list(map(int,input().split()))
    max = lst[0]
    min = lst[0]
    for num1 in lst:
        if max < num1:
            max = num1
    for num2 in lst:
        if min > num2:
            min = num2
    print(f'#{count} {max - min}')