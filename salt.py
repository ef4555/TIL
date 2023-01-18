'''
n개의 소금물을 섞었을 때, 혼합된 소금물의 농도와 양을 계산하는 프로그램 mass_percent.py를 만드시오. 조건    
소금물의 퍼센트 농도와 소금물의 양을 입력하고, Done을 입력하면 혼합물의 퍼센트 농도와 양이 출력되도록 하시오.        
최대 5개의 소금물을 입력할 수 있다. 출력된 혼합물의 퍼센트 농도와 양이 소수점 2자리를 넘어갈 경우, 반올림하여 2번째 자리까지만 나타내시오. 
'''


# 입력 예시
# # mass percent.py 실행 시
# 1.소금물의 농도(%)와 소금물의 양(g)을 입력하십시오: 1% 400g
# 2.소금물의 농도(%)와 소금물의 양(g)을 입력하십시오: 8% 300g
# Done

# 출력 예시
# 4.0% 700.0g


def mass_percent(): 
    count = 0
    salt_list = [] # 입력받은 소금물의 농도 저장하는 리스트
    water_list = [] # 입력받은 소금물의 소금물의 양 저장하는 리스트 
    while count <= 4: # 입력 받은 농도와 소금물의 값이 5개가 될때까지 반복
        a = input(f'{count+1}. 소금물의 농도(%)와 소금물의 양(g)을 입력하십시오: ').split('% ') # 입력받은 문자에서 농도값에 %를 분리
        if a == ['done']:
            break # 'done'입력시 반복 종료
        else: 
            count += 1
            salt_list.append(a[0][0]) # 입력받은 문자에서 농도값만 salt_list 리스트에 저장
            water_list.append(a[1]) # 입력받은 문자에서 소금물의 양만 water_list 리스트에 저장
    print(salt_list)
    print(water_list)
    value1 = 0 # 혼합물의 소금의 양 저장하는 변수
    for c1 in range(0, count):
        value1 += int(salt_list[c1])*int(water_list[c1].replace('g', ''))/100 #혼합물의 소금의 양 계산하여 value에 저장
    print(value1)
    new_water = 0
    for c2 in range(0, count):
        new_water += int(water_list[c2].replace('g', '')) # 혼합물의 소금물의 양 계산하여 new_water에 저장
    print(new_water)
    new_salt_water = round(value1*100/new_water, 2)# 혼합물의 농도 계산하여 new_walt_water에 저장
    
    print(f'{new_salt_water}% {new_water}g')

    

    
mass_percent()
