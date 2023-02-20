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
    # print(st)
    cnt = 0
    stack = []
    for i in range(len(st)):
        if st[i] == '(': # ( 이면 무조건 추가
            stack.append(st[i])
        elif st[i] == ')': # ) 일경우 두가지 케이스 존재. 레이저일수도 아니면 철근이 끝난 것일수도
            if st[i - 1] == '(': # 읽는 문자열 i-1번째에 ( 가 나온다면 레이저니까 쌓인 철근수 추가
                stack.pop()
                cnt += len(stack)
            elif st[i - 1] == ')': # 앞에 ) 가 있었다면 철근이 한 단계 줄어드는 것이니까 철근 스택 갱신하고 cnt에 1추가
                stack.pop()
                cnt += 1
    print(f'#{tc} {cnt}')







