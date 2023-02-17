'''
카운트 배열을 이용한다
1. 방번호대로 만들면 모든 중복을 찾을 수 없겠구나
2. 방이 아니라 복도를 기준으로 만들어야겠구나
0~199번까지 쓰인다.
(방번호-1)해서 2로 나누면 내가 쓰는 복도 번호가 된다.(복도가 양쪽에 있으니까)
시작 복도 번호~끝복도 번호: 누적 cnt 표시
최대값 찾기

모두 값이 0인경우?
모두 값이 max인 경우?
음수 포함되어있나?
정렬 안되어있나?
값이 1개인가?

'''
# 놓쳤을때는 범위를 살펴보고 숨겨진 테스트케이스가 무엇인지 파악
# s와 e가 오름차순으로 온다는 말이 없다
import sys
sys.stdin = open('rt.txt')
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    cnts = [0]*200
    for _ in range(N):
        s, e = map(int, input().split())
        if s > e:
            s, e = e, s
        for j in range((s-1)//2, (e-1)//2+1):
            cnts[j] += 1
    ans = max(cnts)
    print(f'#{tc} {ans}')