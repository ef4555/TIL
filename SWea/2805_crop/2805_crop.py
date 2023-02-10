'''
N X N크기의 농장이 있다.

이 농장에는 이상한 규칙이 있다.

규칙은 다음과 같다.


   ① 농장은 크기는 항상 홀수이다. (1 X 1, 3 X 3 … 49 X 49)

   ② 수확은 항상 농장의 크기에 딱 맞는 정사각형 마름모 형태로만 가능하다.



                                         
1 X 1크기의 농장에서 자라는 농작물을 수확하여 얻을 수 있는 수익은 3이다.

3 X 3크기의 농장에서 자라는 농작물을 수확하여 얻을 수 있는 수익은 16 (3 + 2 + 5 + 4 + 2)이다.

5 X 5크기의 농장에서 자라는 농작물의 수확하여 얻을 수 있는 수익은 25 (3 + 2 + 1 + 1 + 2 + 5 + 1 + 1 + 3 + 3 + 2 + 1)이다.

농장의 크기 N와 농작물의 가치가 주어질 때, 규칙에 따라 얻을 수 있는 수익은 얼마인지 구하여라.


[제약 사항]

농장의 크기 N은 1 이상 49 이하의 홀수이다. (1 ≤ N ≤ 49)

농작물의 가치는 0~5이다.


[입력]

가장 첫 줄에는 테스트 케이스의 개수 T가 주어지고, 그 아래로 각 테스트 케이스가 주어진다.

각 테스트 케이스에는 농장의 크기 N과 농장 내 농작물의 가치가 주어진다.


[출력]

각 줄은 '#t'로 시작하고, 공백으로 농장의 규칙에 따라 얻을 수 있는 수익을 출력한다.

(t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)
'''

# 문자열로 그대로 받고 인덱스를 좌표처럼 써서 풀어보았는데 나중에 합해야 해서 
# 정수로 바꿔주는 과정이 필요해서 별로였다
# 숫자로 받았으면 마지막 for문 필요없이 sum으로 바로 합했을듯

import sys
sys.stdin = open('crop.txt')
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    batt_garo =[[0]*N for _ in range(N)]
    for y in range(N):
        c = list(input())
        batt_garo[y] = c

    l = N//2 # N값의 중간값(인덱스 기준)
    hap = []
    for i in range(l):
        print(batt_garo[i][l-i:l+i+1])
        hap += (batt_garo[i][l-i:l+i+1])
    for j in range(l+1):
        print(batt_garo[l+j][j:N-j])
        hap += (batt_garo[l+j][j:N-j])
    money = 0
    for k in hap:
        money += int(k)
    print(f'#{tc} {money}')