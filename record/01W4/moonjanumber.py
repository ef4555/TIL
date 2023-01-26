# 주어진 문자열에서 숫자, 문자, 기호가 
# 각각 몇개인지를 판단하는 함수를 작성해보세요

def check(a):
    a_count = 0
    digit_count = 0
    symbol_count = 0

    for i in a:
        print(i)
        if i.isalpha():
            a_count += 1
        elif i.isdigit():
            digit_count += 1
        else:
            symbol_count += 1
    return (a_count, digit_count, symbol_count)

s = 'aaaa-1-2111!!!'

a_count, digit_count, symbol_count = check(s) # 리턴값이 3개 이므로 3개의 변수에 나눠담을 수 있다.
print(f'문자는 {a_count}개, 숫자는 {digit_count}개, 기호는 {symbol_count}개')
# 출력 