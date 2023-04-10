'''
0~9 사이의 숫자 카드에서 임의의 카드 6장을 뽑았을 때, 3장의 카드가 연속적인 경우를 run이라고 하고, 
3장의 카드가 동일한 번호를 갖는 경우를 triplet이라고 한다

그리고 6장의 카드가 run과 triplet으로만 구성된 경우를 baby gin 이라고 한다

6자리 숫자를 입력받아 
baby gin여부를 판단하는 프로그램을 작성하여라


'''


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