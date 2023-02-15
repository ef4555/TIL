'''
문자열로 이루어진 계산식이 주어질 때, 이 계산식을 후위 표기식으로 바꾸어 계산하는 프로그램을 작성하시오.

예를 들어

“3+4+5+6+7”

라는 문자열로 된 계산식을 후위 표기식으로 바꾸면 다음과 같다.

"34+5+6+7+"

변환된 식을 계산하면 25를 얻을 수 있다.

문자열 계산식을 구성하는 연산자는 + 하나뿐이며 피연산자인 숫자는 0 ~ 9의 정수만 주어진다.

[입력]

각 테스트 케이스의 첫 번째 줄에는 문자열 계산식의 길이가 주어진다. 그 다음 줄에 문자열 계산식이 주어진다.

총 10개의 테스트 케이스가 주어진다.

[출력]

#부호와 함께 테스트 케이스의 번호를 출력하고, 공백 문자 후 답을 출력한다.

'''



import sys
sys.stdin = open('cal2.txt')
T = 10
for tc in range(1, T+1):
    # 코드로 구현
    N = int(input())
    infix = input()
    stack = []
    result = ''
    # 변환할 식을 순회
    for token in infix:
        # 토큰이 피연산자인 경우
        if token.isdecimal():
            result += token

        # 토큰이 연산자인 경우
        else:
            # stack이 비어있는 경우, stack에 push
            if not stack:  # if len(stack) == 0
                stack.append(token)


            # 스택이 비어있지 않은 경우
            else:
                # (는 incoming 우선순위가 가장 높음.
                if token == '(':
                    stack.append(token)
                # )는 (가 나올때까지 stack에서 pop, result에 append
                elif token == ')':
                    while stack[-1] != '(':
                        result += stack.pop()
                    stack.pop()
                # incoming 우선순위가 2인 경우
                elif token == '*' or token == '/':
                    # stack의 top의 토큰이 우선순위가 낮을 때까지 stack pop, result에 append
                    while stack and stack[-1] in '*/':
                        result += stack.pop()
                    stack.append(token)

                # incoming 우선순위가 1인 경우
                elif token == '+' or token == '-':
                    # stack의 top의 토큰이 우선순위가 낮을 때까지 stack pop, result에 append
                    # (가 아닌 경우 모두 동치
                    while stack and stack[-1] != '(':
                        result += stack.pop()
                    stack.append(token)

    while stack:
        result += stack.pop()

    # 후위연산자를 계산하는 부분
    cal_stack = []
    cal_result = ''
    for word in result:
        if word.isdecimal(): # 피연산자
            cal_stack += word # 스택에 push
        else: # 연산자이면
            while len(cal_stack) > 1: # 스택에 1개 초과로 있으면
                a = cal_stack.pop()
                b = cal_stack.pop() # 두 개 뽑아서 더해준다.
                if word == '+': # 문자열이 '+'라면 연산자 +로 바꿔줌,
                    cal_stack.append(int(a)+int(b))
            # 스택에 원소 1개만 남을때까지 반복된다


    print(f'#{tc} {cal_stack[0]}')