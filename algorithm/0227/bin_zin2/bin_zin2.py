import sys
sys.stdin = open('sample_input (1).txt')
T = int(input())
for t in range(1, T+1):
    answer = ''
    # 계산해야 하는 숫자 받기
    number = float(input())
    # 나누기 위한 값
    sub_num = 1
    for _ in range(12): # 최대 12자리까지 출력
        # 진행이 될수록 크기는 반절이 된다.
        sub_num *= 0.5
        # 값을 빼보았을때 0보다 크다면 뺀고 결과출력
        if number - sub_num >= 0:
            answer += '1'
            number -= sub_num
            if not number: # number가 0이면 반복 종료
                break
        else:
            # 계산이 안된다면 0추가
            answer += '0'
    # 모든 반복문이 끝났는데 값이 남아있다면 overflow
    if number:
        answer = 'overflow'
    print(f'#{t + 1} {answer}')
