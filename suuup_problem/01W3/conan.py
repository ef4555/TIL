'''
김코딩이 일하고 있는 박물관에 도둑이 들었다. 박물관 입구와 출구에 센서가 있다. 센서는 지나가는 사람이 누구인지 인지하여 방문자를 기록한다. 입장 기록은 <code>entry_record</code> list에, 퇴장 기록은 <code>exit_record</code> list에 아래처럼 정리 되어 있다. 주어진 조건으로 분석하여 수상한 사람을 분별하라.
많이 방문한 사람이 도둑일 가능성이 높다. 가장 많이 입장한 세 사람을 찾아 출력하라.
입장 횟수와 퇴장 횟수의 차이가 0이어야 정상이다. 횟수의 차이가 있을 경우 정말 수상하다. 입장 횟수와 퇴장 횟수가 같지 않은 사람을 분별하여 출력하라.
제약 조건: <code>collection</code> 모듈의 <code>Counter</code> 객체를 활용해야 한다.
'''
entry_record = ['이싸피', '박장고', '조실습', '이싸피', '조실습', '오디비', '임온실', '조실습', '조실습', '이싸피', '안도둑', '임온실', '최이썬', '오디비', '안도둑', '염자바', '박장고', '조실습',
                '최이썬', '조실습', '염자바', '박장고', '임온실', '임온실', '이싸피', '임온실', '오디비', '조실습', '염자바', '임온실', '박장고', '최이썬', '안도둑', '염자바', '임온실', '박장고', '이싸피', '안도둑',
                '임온실', '오디비', '최이썬', '안도둑', '이싸피', '오디비', '안도둑', '이싸피', '박장고', '박장고', '안도둑', '안도둑', '안도둑', '염자바', '최이썬', '오디비', '오디비', '최이썬', '이싸피', '임온실', '안도둑']

exit_record = ['최이썬', '조실습', '이싸피', '안도둑', '임온실', '안도둑', '이싸피', '오디비', '염자바', '박장고', '최이썬', '이싸피', '염자바', '염자바', '박장고', '임온실', '이싸피',
               '박장고', '안도둑', '염자바', '이싸피', '조실습', '조실습', '임온실', '박장고', '이싸피', '조실습', '박장고', '오디비', '안도둑', '조실습', '임온실', '안도둑', '안도둑', '임온실', '조실습', '최이썬', '안도둑', '임온실',
               '염자바', '이싸피', '임온실', '안도둑', '오디비', '안도둑', '오디비', '임온실', '염자바', '임온실', '박장고', '조실습', '이싸피', '최이썬', '최이썬', '오디비', '오디비', '염자바', '오디비', '안도둑', '박장고']

import collections

a = collections.Counter(entry_record) # 누가 몇번 입장했는지
b = collections.Counter(exit_record) # 누가 몇번 퇴장했는지
print(a)
print(b)
entry_list = list(a)
entry_dict = dict(a)

exit_list = list(b)
exit_dict = dict(b)
print(sorted(entry_dict.items(), key=lambda x : x[1]))
s_list = sorted(entry_dict.items(), key=lambda x : x[1])
top_list1 = [] # 입장기록 TOP3의 이름을 저장할 리스트
top_list2 = [] # 입장기록 TOP3의 횟수를 저장할 리스트
for t in range(1,4):
    top_list1.append(s_list[-t][0])
    top_list2.append(s_list[-t][1])
'''
top_1_name = s_list[-1][0]
top_2_name = s_list[-2][0]
top_3_name = s_list[-3][0]
top_1_time = s_list[-1][1]
top_2_time = s_list[-2][1]
top_3_time = s_list[-3][1]
'''

print(top_list1)
print(top_list2)
print(f'입장 기록 많은 Top3\n{top_list1[0]} {top_list2[0]}회\n{top_list1[1]} {top_list2[1]}회\n{top_list1[2]} {top_list2[2]}회')

for i in entry_list:
    odd1 = 0
    odd2 = 0
    if entry_dict[i] > exit_dict[i] :
        odd1 = entry_dict[i]-exit_dict[i]
        print(f'{i}은 입장 기록이 {odd1}회 많아 수상합니다.')
    elif entry_dict[i] < exit_dict[i]:
        odd2 = exit_dict[i]-entry_dict[i]
        print(f'{i}은 퇴장 기록이 {odd2}회 많아 수상합니다.')
    else:
        pass