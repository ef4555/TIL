'''
문자열 2개를 전달 받아 두 문자열의 
각 문자에 대응되는 아스키 숫자들의 합을 비교하여 
더 큰 합을 가진 문자열을 반환하는 get_strong_word 함수를 작성하시오.
'''

def get_strong_word(a, b):
    total_a = 0
    total_b = 0
    strong_name = 0
    s_name = 0
    for char in a:
        total_a += ord(char)
    for c in b:
        total_b += ord(c)
    print(total_a)
    print(total_b)
    if total_a > total_b:
        strong_name = total_a
        s_name = a
    else:
        strong_name = total_b
        s_name = b
    return s_name
     

print(get_strong_word('delilah', 'dixon')) # delilah