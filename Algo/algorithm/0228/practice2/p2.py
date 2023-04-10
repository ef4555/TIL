# 01D06079861D79F99F
# 0F97A3
arr = input()
for x in range(len(arr)):
    num = int(arr[x], 16) # 10진수로 바꾸고
    # 10진수에서 2진수로 바꾸기
# num = 0 -> num = 0000
    num = bin(num).replace('0b', '')
    while len(num) != 4:
        num = '0' + num
    print(num)
'''
for j in range(3,-1,-1):
    bit = 1 if num&(1<<j) else 0
    print(bit, end = '')
print(' ', end = '')
'''