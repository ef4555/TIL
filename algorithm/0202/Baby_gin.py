T = int(input())
count = 0
for u in range(0, T):
    tri = run = 0
    num = int(input())
    c = [0]*12
    for i in range(6):
        c[num % 10] += 1
        num //= 10

    i = 0
    while i < 10 :
        if c[i] >= 3 : # triplete 조사 후 데이터 삭제
            c[i] -= 3
            tri += 1
            continue
        if c[i] >= 1 and c[i+1] >= 1 and c[i+2] >= 1: #run 조사 후 데이터 삭제
            c[i] -= 1
            c[i + 1] -= 1
            c[i + 2] -= 1
            run += 1
            continue
        i += 1
    count += 1

    if run + tri == 2 : print(f'#{count} 1')
    else :
        print(f'#{count} 0')