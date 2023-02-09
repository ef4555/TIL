num = input('100으로 나눌 값을 입력하시오 : ')
try:
    print(100/int(num))
except (ValueError):
    print('숫자를 입력해줘')
except (ZeroDivisionError):
    print('0 이외의 숫자를 입력해줘')
except:
    print('무슨이유인지 모르지만 에러 발생')


