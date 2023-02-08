import sys
sys.stdin = open('moon_bi.txt')
T = int(input())
for tc in range(1, T+1):
    str1 = input()
    str2 = input()
    moon = False
    if str1 in str2: # in 사용 문자열 안에 있으면
        moon = True
    '''
    for i in range(len(str2)):
        if str2[i] == str1[0]: # str2 순회하다가 str1의 첫번째 글자 발견하면 
            if str1 == str2[i:i+len(str1)]: # 그 뒤에 len(str1)의 글자가 str1이랑 같은지 판단
                moon = True
    '''

    print(f'#{tc} {int(moon)}')