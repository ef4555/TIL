'''
NxN 배열에 숫자가 들어있다. 한 줄에서 하나씩 N개의 숫자를 골라 합이 최소가 되도록 하려고 한다. 단, 세로로 같은 줄에서 두 개 이상의 숫자를 고를 수 없다.

조건에 맞게 숫자를 골랐을 때의 최소 합을 출력하는 프로그램을 만드시오.

첫 줄에 테스트 케이스 개수 T가 주어진다.  1≤T≤50

다음 줄부터 테스트 케이스의 첫 줄에 숫자 N이 주어지고, 이후 N개씩 N줄에 걸쳐 10보다 작은 자연수가 주어진다. 3≤N≤10

각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 합계를 출력한다.



3
9 4 7
8 6 5
5 3 7
5
5 2 1 1 9
3 3 8 3 1
9 2 8 8 6
1 5 7 8 3
5 5 4 6 8
'''
import sys
sys.stdin = open('bae_min_hap.txt')

def dfs(row, n, now_sum, visited):
    global min_sum  # 최소 합을 전역변수로 선언
    if row == n:  # row가 배열의 수와 일치하면
        if now_sum < min_sum:
            min_sum = now_sum  # 현재합이 더 작으면 대체
    elif now_sum > min_sum:
        return  # 현재 부분합이 더 크면 탐색 중지

    else:
        for col in range(n):
            if not visited[col]:  # 방문 전인 칼럼
                visited[col] = 1  # 방문 처리
                # 다음 열로 넘어가고 now_sum에 값을 더해주고, visited 갱신
                dfs(row + 1, n, now_sum + lst[row][col], visited)
                visited[col] = 0  # 함수 적용 후 초기화(재검색 할 수 있도록)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    lst = [[0] * N for _ in range(N)]
    for l in range(N):
        lst[l] = list(map(int, input().split()))
    print(lst)
    min_sum = 100
    visited = [[0]*N for _ in range(N)]

    dfs(0, N, 0, visited)
    print(visited)
    print(f'#{tc} {min_sum}')





