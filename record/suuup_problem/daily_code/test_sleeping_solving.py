test_status = {
    '김싸피': 'solving',
   	'이코딩': 'solving',
   	'최이썬': 'cheating',
   	'오디비': 'sleeping',
   	'임온실': 'cheating',
   	'조실습': 'solving',
   	'박장고': 'sleeping',
   	'염자바': 'cheating'
}
cheat_list = []
sleep_list = []
for i in test_status:
    # print(i)
    # print(test_status[i])
    if test_status[i] == 'cheating':
        cheat_list.append(i)
print(sorted(cheat_list))
for t in cheat_list:
    del test_status[t]
for s in test_status:
    if test_status[s] == 'sleeping':
        sleep_list.append(s)
for st in sleep_list:
    test_status[st] = 'solving'

print(f'test_status = {test_status}')
        