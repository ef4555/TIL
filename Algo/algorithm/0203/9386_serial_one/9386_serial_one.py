import sys

sys.stdin = open('jumjum.txt')

T = int(input())
for test_case in range(1, T + 1):
    N = int(input()) # 테스트 케이스 수열의 길이
    lst = list(map(int, input())) # 테스트 케이스 수열
    cnt = ans = 0 # 연속한 1의 최댓값을 저장할 변수
    for i in range(N): # 수열의 길이만큼 반복
        if lst[i] == 0: # 0이 나오면 0으로 초기화
            cnt = 0
        else:
            cnt += 1 # 1이 나오면 1 추가
            if ans < cnt: # 카운팅한 수열의 길이가 저장해둔 연속한 1의 최댓값보다 작으면
                ans = cnt # 최댓값 갱신


    print(f'#{test_case}', ans)