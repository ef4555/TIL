# A.    입력 예시 
# ['eat','tea','tan','ate','nat','bat']

# B.    출력 예시 
# [ ['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat'] ] 


def group_anagrams(string_list):
# 정렬된 문자열 저장 리스트
    list2 = ["eat","tea","tan","ate","nat","bat"] 
# 문자열 정렬후 다시 1차원으로 합치기
    for i in range(len(string_list)): 
    # 정렬된 리스트로 만들어진 문자열을 하나의 문자열로 합치고 그것을 새 리스트에 매달기
        list2.append(''.join(sorted(string_list[i]))) 

# 애너그램 정렬한거 저장할 문자열
    list3 = [] 
    for i in range(len(list2)):
        if list2[i] not in list3[:i]:
            list3.append(list2[i])
    # print(list3)
    # 결과물 2차원 리스트 생성 집합으로 다른거 몇개인지 확인
    output_list = [[] for i in range(len(set(list2)))] 

#리스트2에 있는 문자가 리스트3 몇번째 위치에 있는지 확인, 그 위치와 처음 받은 리스트에 문자를 가져와 output_list에 저장.
    for i in range(len(list2)):
        output_list[list3.index(list2[i])].append(string_list[i])
# print(output_list)
# output_list 리턴받기
    return output_list


a = group_anagrams(str_list)
print(a)

