# 입력 예시
# 2015
# 8
# 31

# 출력 예시 
# 경고 월요일입니다.
# {'년': 2015, '월': 8, '일': 31, '요일': '월요일'}

import calendar

year = int(input('년도를 입력하세요 : ')) # 년도 입력 받기
tm_dict = {'년': 0, '월': 0, '일': 0, '요일': 0} # 결과값 저장하는 딕셔너리
days = ['월요일', '화요일', '수요일', '목요일', '금요일', '토요일', '일요일'] # 요일 분류하는 리스트

def yoon(t): # 입력받은 년도가 윤년인지 파악
        if t % 4 == 0 and t % 100 != 0: 
            print('윤년입니다.')
            return(yoon(int(input('다시 입력해주세요 : '))))
            yoon()
        elif t % 400 == 0:
            print('윤년입니다.')
            return(yoon(int(input('다시 입력해주세요 : '))))
        else:
            print('윤년이 아닙니다.')
            return(t)

a = yoon(year) # 윤년이 아닌 년도 변수 a에 저장
c = calendar.calendar(a) 
print(c) # 캘린더 모듈 이용하여 해당 년도 달력 출력
month = int(input('월 입력하세요 : ')) # 달 입력
date = int(input('일을 입력하세요 : ')) # 일 입력

tm = [a, month, date] # 년, 월, 일 저장하는 리스트 
d = calendar.weekday(a, month, date) # 해당 날짜가 월요일인지 판별하기 위해 캘린더 모듈 이용하여 해당 날짜 코드 받기
if d == 0:
    print('경고 월요일입니다.') #월요일이면 경고 출력
tm_dict['년'] = tm[0] 
tm_dict['월'] = tm[1]
tm_dict['일'] = tm[2]
tm_dict['요일'] = days[d] #tm_dict에 년도, 달, 일, 요일 저장
print(tm_dict)