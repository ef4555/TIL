'''

어린이 알고리즘 교실의 선생님은 경우의 수 놀이를 위해,
그림처럼 가로x세로 길이가 10x20, 20x20인 직사각형 종이를 잔뜩 준비했다.


그리고 교실 바닥에 20xN 크기의 직사각형을 테이프로 표시하고,
이 안에 준비한 종이를 빈틈없이 붙이는 방법을 찾아보려고 한다. N이 30인 경우 다음 그림처럼 종이를 붙일 수 있다.


10의 배수인 N이 주어졌을 때, 종이를 붙이는 모든 경우를 찾으려면
테이프로 만든 표시한 영역을 몇 개나 만들어야 되는지 계산하는 프로그램을 만드시오.
직사각형 종이가 모자라는 경우는 없다.


[입력]

첫 줄에 테스트 케이스 개수 T가 주어진다.  1≤T≤50
다음 줄부터 테스트 케이스 별로 N이 주어진다. 10≤N≤300, N은 10의 배수

[출력]

각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.
'''

import sys
sys.stdin = open('paper.txt')
T = int(input())  # test case

# 바닥 케이스 존재
# 점화식의 성질 존재
# 남은 길이가 20이면 앞선 모든 경우에 * 2의 경우의 수 존재
# 남은 길이가 10이면 앞선 모든 경우의 수 만큼 경우의 수 존재
# paper(n - 10) + (2 * paper(n - 20))
def paper(n):
    if n == 10:
        return 1
    elif n == 20:
        return 3
    elif n < 10:
        return 0
    else:
        return paper(n - 10) + (2 * paper(n - 20))


for tc in range(1, T + 1):
    N = int(input())  # 바닥 길이, 10의 배수만 들어올 수 있다.

    print(f"#{tc} {paper(N)}")

'''
# import sys
# sys.stdin = open("sample_input_2.txt", "r")
# T = int(sys.stdin.readline().rstrip())
# for tt in range(1, T+1):
#     n = int(sys.stdin.readline().rstrip())
T = int(input())
for tt in range(1, T+1):
    n = int(input())
    dp = [1, 3]
    for i in range(2, n//10):
        dp.append(dp[i-2]*2 +dp[i-1])
    print(dp)
    print(dp[-1])
'''

'''
def paper(n):
    q = n // 10
    memo = [0] * (q + 1)
    memo[0] = memo[1] = 1
 
    for i in range(2, q + 1):
        memo[i] = memo[i-1] + memo[i-2] * 2
 
    return memo[-1]
 
T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    print(f'#{tc}', paper(n))
'''





