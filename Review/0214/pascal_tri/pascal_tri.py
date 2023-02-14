'''
크기가 N인 파스칼의 삼각형을 만들어야 한다.

파스칼의 삼각형이란 아래와 같은 규칙을 따른다.

1. 첫 번째 줄은 항상 숫자 1이다.

2. 두 번째 줄부터 각 숫자들은 자신의 왼쪽과 오른쪽 위의 숫자의 합으로 구성된다.

N이 4일 경우,




N을 입력 받아 크기 N인 파스칼의 삼각형을 출력하는 프로그램을 작성하시오.


[제약 사항]

파스칼의 삼각형의 크기 N은 1 이상 10 이하의 정수이다. (1 ≤ N ≤ 10)


[입력]

가장 첫 줄에는 테스트 케이스의 개수 T가 주어지고, 그 아래로 각 테스트 케이스가 주어진다.

각 테스트 케이스에는 N이 주어진다.


[출력]

각 줄은 '#t'로 시작하고, 다음 줄부터 파스칼의 삼각형을 출력한다.

삼각형 각 줄의 처음 숫자가 나오기 전까지의 빈 칸은 생략하고 숫자들 사이에는 한 칸의 빈칸을 출력한다.

(t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)
'''
import sys
sys.stdin = open('pascal_tri.txt')
T = int(input())

memo = [[0 for _ in range(11)] for _ in range(11)] # 파스칼의 삼각형 최대 줄(10)을 주어줬으므로 +1만큼 하여 빈 2차원 리스트를 만든다.
# 인덱스 혼돈 방지,
for i in range(10): # 0부터 9까지 (한줄씩 순회)
    for j in range(i + 1): # 0 00, 1 01, 2 012 ... 한 행을 순회하면서(파스칼의 삼각형은 다음 줄이 i+1로 늘어남)
        if j == 0 or i == j: # 시작점이거나 끝자리이면
            memo[i][j] = 1 # 1을 추가함
        else: # 시작점이거나 끝이 아닌 경우
            memo[i][j] = memo[i - 1][j - 1] + memo[i - 1][j] # 자신의 왼쪽과 오른쪽 위 숫자의 합으로 구성된다. 인덱스상으로는 열 [i - 1]번째 행 [j - 1], [j]번째의 합

# 10줄짜리 파스칼 삼각형 완성


for tc in range(1, T + 1): # 테스트케이스
    N = int(input()) # 출력할 파스칼 삼각형 크기
    print(f'#{tc}') # 테스트 케이스 출력

    for i in range(N): # 파스칼 삼각형 크기만큼 반복
        for j in range(i + 1): # 0 00, 1 01, 2 012 ... 출력할 행을 점점 늘려가면서(파스칼의 삼각형은 다음 줄이 i+1로 늘어남)
            print(f'{memo[i][j]}', end=' ') # 출력
        print()
