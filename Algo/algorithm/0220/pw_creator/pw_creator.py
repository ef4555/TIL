import sys
sys.stdin = open('pw.txt')
T = 10
for tc in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))
    print(lst)
    i = 1
    front = 0
    while lst[-1] > 0: # 맨 뒷자리 숫자가 0 초과일때까지
        if i == 6: # i 가 1사이클을 돌면 초기화
            i = 1
        else:
            lst.append(lst[front] - i) # front 숫자에 i를 빼고 rear + 1 위치로 추가
            front += 1
            i += 1
    print(f'#{N}', *lst[-8:-1], 0 ) # 7자리 숫자의 뒤에 0을 붙여줌