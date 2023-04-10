import sys
sys.stdin = open('chobo_hm.txt')
T = int(input())
for tc in range(1, T+1):
    hm = input()
    c = 0
    if hm == hm[::-1]:
        c = 1
    print(f'#{tc} {c}')

'''
# 이현도님 풀이
# 반갈해서 중심으로 끝에서 중심으로 옮기면서 같은지 확인

T = int(input())
for test_case in range(1,T+1):
    word = input()
    idx = 0
    for idx in range(int(len(word)/2)):
        if word[idx] !=word[-idx-1]: # 왼쪽끝과 오른쪽 끝 비교
            print(f'#{test_case} 0')
            break
    else:
        print(f'#{test_case} 1')
'''
'''
# 김영석님 코드
# 제일 짧음

for tc in range(1, int(input())+1):
    s = input()
    print(f'#{tc} {1 if s == s[::-1] else 0}')


[[print(f'#{tc+1} {1 if s == s[::-1] else 0}') for s in [(input())]] for tc in range(int(input()))]

'''
# 
'''
