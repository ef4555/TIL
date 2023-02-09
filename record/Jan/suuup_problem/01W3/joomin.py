# A. 입력예시
# print(de_identify('970103-1234567'))
# print(de_identify('8611232345678'))

# B. 출력예시
# 970103*******
# 861123******* 


def de_identify(id):
    a = id.replace('-', '')
    b = a[0:6] + '*'*7
    return b

print(de_identify('970103-1234567'))
print(de_identify('8611232345678'))
