import random
import time


list_03 = [
'조재웅', '김솔', '이현도', '최예훈', 
'이명우', '김연재', '김영석', '엄한결',
'황재천', '고서영', '김유진', '김동욱',
'김동훈', '고세훈', '배희진', '박영서',
'연제정', '김동준', '유진욱', '류나연',
'임휘진', '서인덕', '박도현', '조현기',
'김재석', '하재우', '정준혁', '정예륜'
]

def not_here(): # 결석한 사람 여부를 판별하여 반 리스트에서 결석한 사람의 이름을 삭제하는 함수
    saram = input('오늘 결석한 사람이 있나요?(예/아니오) : ')
    if saram == '예': # 결석한 사람이 있어서 예를 입력하면
        not_here_saram = [] # 결석한 사람의 이름을 담을 리스트
        try:
            saram_num = int(input('결석한 사람 수를 입력해주세요(숫자만 입력) : '))  # 결석한 사람의 수를 입력받는다
            if saram_num != 0: # 결석한 사람이 있으면(결석한 사람의 수가 0이 아니면)
                count = 1 # 반복 횟수를 카운트 할 변수
                print('결석한 사람을 순차적으로 입력해주세요, 처음으로 돌아가시려면 restart 입력해주세요')
                while count <= saram_num: # 반복 횟수를 카운트 할 변수가 입력받은 사람의 수가 될 때까지 반복한다.
                    time.sleep(0.3)
                    saram_name = input(f'결석한 사람 이름을 입력해주세요 #{count} : ') # 결석한 사람의 이름을 변수에 저장한다.
                    if saram_name in list_03 and saram_name not in not_here_saram: # 입력받은 사람의 이름이 우리 3반 이름 리스트에 존재하면
                        not_here_saram.append(saram_name) # 결석한 사람의 이름을 담는 리스트 not_here_saram에 입력받은 이름 저장한다.
                        count += 1 # 반복 횟수에 1을 더한다.
                    elif saram_name in not_here_saram:
                        print('이미 입력한 인원입니다.') # 입력받은 이름이 이미 입력한 이름이며 다시  입력하라고 출력한다.
                    elif saram_name not in list_03 and saram_name != 'restart':
                        print('이름을 잘못 입력하셨습니다. 해당 인원은 서울3반이 아닙니다.')# 입력받은 이름이 3반 명단에 없으면 다시 입력하라고 출력한다.
                    elif saram_name == 'restart':
                        print('다시 시작합니다.')
                        return not_here()

                yn_count = 0 # 예 아니오를 판별하는 변수 
                while yn_count == 0: 
                    saram_yes_no = input(f'결석한 사람은 {not_here_saram}이고 총{len(not_here_saram)}명입니다. 맞습니까?(예/아니오) : ')
                    if saram_yes_no == '예': 
                        for saram in not_here_saram: # 결석한 사람 명단에 있는 이름을
                            list_03.remove(saram) # 3반 명단 리스트에서 제거
                        yn_count += 1
                    elif saram_yes_no == '아니오':
                        print(f'결석한 사람을 다시 입력해주세요')
                        return not_here()
                    else:
                        print(f'예/아니오로 입력해주세요')

        except:
            print(f'오류입니다.')
            return not_here()


    elif saram == '아니오': # 결석한 사람이 없어서 아니오를 입력하면
        print('결석한 사람이 없군요! 성실한 3반~')

    else: # 예 아니오로 대답하지 않았을 시
        print('예/아니오로 답해주세요')
        return not_here()

def lunch_div(): # 인원을 랜덤으로 나누는 함수
    try:
        div_saram = int(input('몇명씩 한 조로 나누시겠습니까?(숫자로만 입력해주세요) : ')) 
        if div_saram == 0: # 0을 입력한 경우
            print('0명으로 나눌 수는 없습니다.')
            lunch_div()
        yn_lunch_count = 0 # 입력받은 숫자로 팀을 나눌지 결정하는 변수
        while yn_lunch_count == 0: # yn_lunch_count가 변할때까지
            if len(list_03)%div_saram != 0: # 입력한 수로 인원을 나누었을때 나누어 떨어지지 않고 나머지가 생기는 경우
                yn_saram_div = input((f'{div_saram}명씩 나누면 {len(list_03)//div_saram}개의 조가 생기고, {len(list_03)%div_saram}명으로 이루어진 조가 생기게 됩니다. 그대로 진행하시겠습니까?(예/아니오) : '))
                if yn_saram_div == '아니오': 
                    print('나눌 숫자를 다시 입력해주세요 ')
                    return lunch_div()
                elif yn_saram_div == '예':
                    print('한 조는 더욱 친밀하게 식사하겠네요!') 
                    return div_saram
                else: 
                    print('예/아니오로 다시 입력해주세요 ')

                yn_lunch_count += 1 # yn_lunch_count += 1을 하고 반복문 탈출
                return div_saram
            else:
                print(f'{div_saram}명씩 나누면 {len(list_03)//div_saram}개의 조가 생기고 남는 사람은 없습니다.') # 입력한 수로 인원을 나누었을때 나누어 떨어지는 경우
                yn_lunch_count += 1
                return div_saram
    except:
        print('예/아니오로 다시 입력해주세요')
        return lunch_div()

def ran_bap(num): # 랜덤으로 점심 조를 추출하는 함수
    time.sleep(0.5)
    print('카운트다운 시작!')
    time.sleep(0.8)
    print('두구'*20)
    time.sleep(0.8)
    for sec in range(3,0,-1):
        print(f'{sec}')
        time.sleep(0.7)
    print('랜덤!!')
    time.sleep(0.4)
    while len(list_03) >= int(num): # 3반 명단 리스트의 남은 인원이 나누는 수보다 작아질 때 까지
        team = random.sample(list_03, int(num)) # 랜덤으로 나누는 수만큼 뽑아서 team 변수에 저장
        print(f'{team}끼리 맛점하세요~') # 뽑은 인원을 출력
        time.sleep(0.2)
        print(f'\n')
        for a in team: # 랜덤으로 뽑은 이름들을
            list_03.remove(a) # 3반 명단에서 제거
            if len(list_03) == 0:
                print('즐거운 점심시간~~~~')
    if len(list_03) ==  1: # 3반 명단에 혼자 남게 된 경우
        print(f'그리고 {list_03} 혼밥하세요~')
        print('\n즐거운 점심시간~~~~')
    elif len(list_03) > 1: # 랜덤 점심 팀에 뽑히지 않고 남은 인원
        print(f'{list_03}끼리 맛점하세요~')
        print('\n즐거운 점심시간~~~~')



print('*'*80)
print(f'안녕하세요 랜덤 점심 친구 프로그램입니다.')
print(f'서울 3반의 전체 인원은 {len(list_03)}명 입니다.')
print('*'*80)
not_here()
print(f'현재 있는 인원은 {len(list_03)}명입니다')
ran_bap(lunch_div())
    
    



