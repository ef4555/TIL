T = int(input())
l = []
for test_case in range(1, T + 1):
    a = int(input())
    l.append(a)
p = sum(l)/len(l)
print(f'입력된 값 {l}의 평균은 {p}입니다.')
