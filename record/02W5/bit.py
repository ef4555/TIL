def bit(i):
    output = ''
    for j in range(7, -1, -1): # 맨 끝자리(첫번째)부터 2진법 배치
        output += '1' if i & (1 << j) else '0'
    print(output)

for i in range(-5,  6):
    print("%3d = " %i, end = '')
    bit(i)