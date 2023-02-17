# 5432 쇠막대기 자르기
# if와 elif만 잘해도 im은 통과
# 괄호가 열리면 쇠막대기를 놓는다
# 괄호가 닫히면 레이저
# 쌓여진 쇠막대기 수를 고려해야 함
# 잘려진 쇠막대기의 총 개수 구하기
'''
쌓여있는 쇠막대기 수 cnt
if 괄호가 열리면 '(' cnt += 1 레이저 시작점일수도 있으니까
뒤를 체크해야한다(범위 필요) 앞을 체크 <- 인덱스를 사용

else:
닫히는 괄호라면
    if steel[i-1]이 '('라면 레이저
        cnt -= 1, ans += cnt
        카운트 개수만큼 우르르 늘어남
    else:
        ')' 라면 = 막대기 끝이라면
        cnt -= 1, ans += 1




'''
import sys
sys.stdin = open('steel_cut.txt')

T = int(input())
for tc in range(1, T+1):
    st = input()
    ans = 0
    cnt = 0
    for i in range(len(st)):
        if st[i] == '(': # 막대 시작 또는 레이저
            cnt += 1
        else: # 닫히는 괄호, 바로앞 기호를 확인해야함
            if st[i-1] == '(': # 레이저인 경우
                cnt -= 1 # 앞에게 막대가 아니라 레이저였으니까 오해했으니까 -1 해준다
                ans += cnt
            else:
                cnt -= 1
                ans += 1
    print(f'#{tc} {ans}')

