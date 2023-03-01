a = '0000000111100000011000000111100110000110000111100111100111111001100111'

arr = list(map(int, a))
i = 0
while 7*i < len(a):
    b = a[7*i:7*i+7]
    num = 0
    for k in range(len(b)):
        num += int(b[::-1][k]) * (2**k)
    print(num, end= ' ')

    i += 1
