
import sys
sys.stdin = open('input.txt')

def f(cur_num, change_num, can_stay):
    if cur_num == change_num: # 바꾼 횟수가 바꿔야할 횟수와 같으면 
        record[0] = max(record[0], ''.join(nums)) # 현재 record에 저장된 값과 최댓값
 
        if nums == sorted_nums: # 수동으로 정렬한 값이 정렬되었던 값과 같으면
            found_optimal[0] = True # 최적값 True
 
#     elif found_optimal[0]: # 최대값이면
#         if can_stay: # 중복 없으면
#             return # 함수 끝
#         else: # 중복 있으면 
#             nums[-1], nums[-2] = nums[-2], nums[-1] # 최대값이 아니면 섞어준다
#             f(cur_num + 1, change_num, can_stay) # 한번 섞어주고 재귀
#             nums[-1], nums[-2] = nums[-2], nums[-1] # 다시 원상태로
#  
    else: # 최대값이 아니면
        for i in range(L-1): # 순열로 섞어줌
            for j in range(i+1, L): 
                nums[i], nums[j] = nums[j], nums[i]
                f(cur_num + 1, change_num, can_stay)
                nums[i], nums[j] = nums[j], nums[i] 
 
 
def is_even_permutation(nums, sorted_nums, L):
 
    is_even = True # 홀수인지 체크, 같은지도 체크
 
    while True:
        for i in range(L-1):
            if nums[i] != sorted_nums[i]: # 원래 리스트와 정렬된 리스트의 자리를 비교하면서
                index_different = i # 원래 리스트와 정렬된 리스트가 다른 부분의 인덱스 발견
                break
        else:  
            return is_even # 같은 경우 True
 
        is_even = not is_even # 원래 리스트와 정렬된 리스트가 다르면 is_even은 False됨
 
        for j in range(L-1, -1, -1): # 거꾸로 탐색하면서
            if nums[j] == sorted_nums[index_different]: # 원래 리스트와 정렬된 리스트의 다른 부분의 숫자를 찾음
                index_to_swap = j 
                break
 
        # swap them
        nums[index_to_swap], nums[index_different] = nums[index_different], nums[index_to_swap] # 원래 리스트와 정렬된 리스트의 다른 부분을 서로 바꿔줌
 
 
T = int(input())
for t in range(1, T+1):
    nums, change_num = input().split()
    nums = list(nums) # nums 받은 리스트
    
    change_num = int(change_num) # 정렬 횟수 change_num
    L = len(nums) # 정렬할 리스트 길이 L
 
    sorted_nums = sorted(nums, reverse=True) # 리스트 정렬
 
    # check if it has digits with multiplicity >= 2
    if len(set(nums)) < L: # 중복되는 숫자 있는지 확인
        can_stay = True # 중복되는 숫자 있으면 True
    else:
        can_stay = False # 중복 없으면 False
 
    record = ["0"*L] # 기록할 리스트 ['0'*L]
    found_optimal = [False]
    if L <= change_num: # 리스트 길이가 정렬 횟수보다 작으면
        if can_stay: # 중복 있으면
            record[0] = ''.join(sorted_nums) # 그냥 sort 쓴 리스트가 답이 된다
        else: # 중복 없으면 
            is_even = is_even_permutation(nums, sorted_nums, L) # 받은 리스트, 정렬된 리스트, 리스트 길이
            if is_even: 
                record[0] = ''.join(sorted_nums) # 그대로 
            else: 
                sorted_nums[-1], sorted_nums[-2] = sorted_nums[-2], sorted_nums[-1] # 끝자리 두 부분 자리 바꿔줌
                record[0] = ''.join(sorted_nums)
    else: # 리스트 길이가 정렬할 횟수보다 크면 
        f(0, change_num, can_stay)
 
    print(f'#{t} {record[0]}')