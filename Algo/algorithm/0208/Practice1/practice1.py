'''
문자열을 거꾸로 출력

4
algorithm
life is short
you need python
SSAFY

'''

'''
T = int(input())
for tc in range(1, T+1):
    s = input()
    print(f'#{tc} {s[::-1]}')
'''
T = int(input())
for tc in range(1, T+1):
    s = list(input())
    lst = []
    for i in range(len(s)-1, -1, -1):
        lst.append(s[i])
    print(f'#{tc}', ''.join(lst))