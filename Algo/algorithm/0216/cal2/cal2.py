'''
문자열로 이루어진 계산식이 주어질 때, 이 계산식을 후위 표기식으로 바꾸어 계산하는 프로그램을 작성하시오.

예를 들어

“3+4+5*6+7”

라는 문자열로 된 계산식을 후위 표기식으로 바꾸면 다음과 같다.

"34+56*+7+"

변환된 식을 계산하면 44를 얻을 수 있다.

문자열 계산식을 구성하는 연산자는 +, * 두 종류이며 피연산자인 숫자는 0 ~ 9의 정수만 주어진다.

[입력]

각 테스트 케이스의 첫 번째 줄에는 테스트 케이스의 길이가 주어진다. 그 다음 줄에 바로 테스트 케이스가 주어진다.

총 10개의 테스트 케이스가 주어진다.

[출력]

#부호와 함께 테스트 케이스의 번호를 출력하고, 공백 문자 후 답을 출력한다.
'''

import sys
sys.stdin = open('cal2.txt')
T = 10
for tc in range(1, T+1):
    N = int(input())
    m = input()
    stack = []
    result = ''
    for token in m:
        # 토큰이 피연산자인 경우
        if token.isdecimal():
            result += token
        # 토큰이 연산자인 경우
        else:
            if not stack:
                stack.append(token)
            else:
                if token == '(':
                    stack.append(token)
                elif token == ')':
                    while stack[-1] != '(':
                        result += stack.pop() # (가 나올때까지 스택에 있는 연산자 뽑고
                    stack.pop() # (가 나오면 그거 제거
                elif token == '*' or token == '/':
                    while stack and stack[-1] in '*/':
                        result += stack.pop() # 토큰이랑 같은 순위의 연산자 나올때까지 스택에 있는 연산자 뽑고 결과에 저장
                    stack.append(token) # 토큰 스택에 추가
                elif token == '+' or token == '-':
                    # stack의 top의 토큰이 우선순위가 낮을 때까지 stack pop, result에 append
                    # (가 아닌 경우 모두 동치
                    while stack and stack[-1] != '(':
                        result += stack.pop() # 그 전의 연산자가 곱하기와 나누기일 때, 그 연산자를 처리해주고 그렇지 않으면 스택에 push
                    stack.append(token)
    while stack:
        result += stack.pop()

    cal_stack = []
    cal_giho = []
    for word in result:
        if word.isdecimal(): # 피연산자
            cal_stack.append(word) # 스택에 push
        else: # 연산자이면
            if word != '.':
                cal_giho.append(word)
                while len(cal_stack) > 1: # 스택에 1개 초과로 있으면
                    b = cal_stack.pop()
                    a = cal_stack.pop() # 두 개 뽑아서 더해준다.
                    if word == '+': # 문자열이 '+'라면 연산자 +로 바꿔줌,
                        cal_stack.append(int(a)+int(b))
                        cal_giho.pop()
                        break
                    elif word == '-': # 문자열이 '+'라면 연산자 +로 바꿔줌,
                        cal_stack.append(int(a)-int(b))
                        cal_giho.pop()
                        break
                    elif word == '*': # 문자열이 '+'라면 연산자 +로 바꿔줌,
                        cal_stack.append(int(a)*int(b))
                        cal_giho.pop()
                        break
                    elif word == '/': # 문자열이 '+'라면 연산자 +로 바꿔줌,
                        cal_stack.append(int(a)//int(b))
                        cal_giho.pop()
                        break
    # print(cal_stack)
    # print(cal_giho)
    if len(cal_giho) != 0 or len(cal_stack) != 1: # 안쓰인 연산자가 있거나, 안쓰인 숫자가 있으면
        print(f'#{tc} error') # 에러 발생
    else:
        print(f'#{tc} {cal_stack[0]}')
