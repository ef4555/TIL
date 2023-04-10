import sys
sys.stdin = open('mili.txt')
T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    lst = list(map(int, input().split()))[::-1] # 거꾸로 탐색한다
    print(lst)
    ans = mx = 0 # 답이랑 최대값이랑 0으로 놓고
    for n in lst: # lst에서 최소값 훝으면서
        if mx > n: # 큰 값을 만나면
            ans += mx - n # 최대값의 차
        else: # n값이 mx 값보다 크거나 같으면
            mx = n # 최대값 갱신
        # 인덱스 불러오는 것 없이 값만 쭉 읽어서 처리하므로 더 빠르다.
    print(f'#{test_case} {ans}')