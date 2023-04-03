
while True:
    m = input()
    if m == '0':
        break
    elif m == m[::-1]:
        print('yes')
    else:
        print('no')
