
def find_set(x): # x가 속한 집합의 대표원소 리턴
    while x != rep[x]: # x == rep[x]가 될때까지
        x = rep[x] # 찾으면 x에 할당하고 반복 끝
    return x  # 리턴
    
def union(x, y): # y의 대표원소가 x의 대표원소를 가리키도록 함
    rep[find_set(y)] = find_set(x)
    rep[y] = find_set(x)


# makeset ()
rep = [i for i in range(6)]
print(rep)

a = find_set(3)
print(a)
print(rep)
union(1, 3)
print(rep)