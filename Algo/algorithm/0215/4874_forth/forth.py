'''

Forth라는 컴퓨터 언어는 스택 연산을 기반으로 하고 있어 후위 표기법을 사용한다. 예를 들어 3+4는 다음과 같이 표기한다.

숫자는 스택에 넣는다.

연산자를 만나면 스택의 숫자 두 개를 꺼내 더하고 결과를 다시 스택에 넣는다.

‘.’은 스택에서 숫자를 꺼내 출력한다.



Forth 코드의 연산 결과를 출력하는 프로그램을 만드시오. 만약 형식이 잘못되어 연산이 불가능한 경우 ‘error’를 출력한다.


[입력]


첫 줄에 테스트 케이스 개수 T가 주어진다.  1≤T≤50


다음 줄부터 테스트 케이스의 별로 정수와 연산자가 256자 이내의 연산코드가 주어진다. 피연산자와 연산자는 여백으로 구분되어 있으며, 코드는 ‘.’로 끝난다.

나눗셈의 경우 항상 나누어 떨어진다.



[출력]


#과 1번부터인 테스트케이스 번호, 빈칸에 이어 계산결과를 정수로 출력하거나 또는 ‘error’를 출력한다.

'''


import sys
sys.stdin = open('forth.txt')
T = int(input())
for tc in range(1, T+1):
    # 코드로 구현
    infix = input().split()
    # 변환할 식을 순회
    # 후위연산자를 계산
    cal_stack = []
    cal_giho = []
    for word in infix:
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
    print(cal_stack)
    print(cal_giho)
    if len(cal_giho) != 0 or len(cal_stack) != 1: # 안쓰인 연산자가 있거나, 안쓰인 숫자가 있으면
        print(f'#{tc} error') # 에러 발생
    else:
        print(f'#{tc} {cal_stack[0]}')

