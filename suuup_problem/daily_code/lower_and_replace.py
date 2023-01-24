
# 입력 예시
s = '@#~I NeVEr DrEamEd AbouT SuCCeSs, i woRkEd foR iT.!>!'

# 출력 예시
# 'I never dreamed about success, i worked for it.'
a = s[3:-3]
b = a.lower()
c = b.replace('i', 'I', 1)
print(c)
