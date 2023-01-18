strs = ["eat", "tea", "tan","ate","nat","bat"]

anagram = {}

for word in strs:
    key = ''.join(sorted(word))
    print(key)
    if key in anagram: # 정렬된 값이 있는경우 
        anagram[key].append(word) # 문자열을 딕셔너리에 value값으로 추가
    else: # 정렬된 값이 없는 경우
        anagram[key] = [] # value값을 빈 리스트로 만든 다음 value를 추가한다
        anagram[key].append(word) 
print(list(anagram.values()))


# https://kbh224.tistory.com/4