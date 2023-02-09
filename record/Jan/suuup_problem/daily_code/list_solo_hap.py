# num_list = [4, 4, 7, 8, 10, 4]
# sum_of_repeat_number(num_list)

# 출력 예시 
#  25

def sum_of_repeat_number(a) :
    b = sorted(a)
    print(b)
    not_joong = []
    hap = 0
    for i in b:
        if i not in not_joong:
            not_joong.append(i)
    print(not_joong)
    for v in not_joong:
        if b.count(v) == 1:
            hap += v
    return(hap)

        
        
    

print(sum_of_repeat_number([4, 4, 7, 8, 10, 4]))
