import sys

sys.stdin = open('jomang.txt')

T = 10
count = 0
for i in range(1,T+1):
    gun_num = int(input())
    gun_mool = list(map(int, input().split()))
    jomang_num = 0
    idx = 2
    bum = 2
    while idx < gun_num-2:
        side = gun_mool[idx-bum:idx+bum+1]
        side.remove(gun_mool[idx])
        max1 = 0
        for num1 in side:
            if max1 < num1:
                max1 = num1
        if max1 < gun_mool[idx]:
            jomang_num += gun_mool[idx]-max1
            idx += 3
        else:
            idx += 1
    count += 1
    print(f'#{count} {jomang_num}')
