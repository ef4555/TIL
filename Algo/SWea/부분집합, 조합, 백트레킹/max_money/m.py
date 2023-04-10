import sys
sys.stdin = open('input.txt')

# 1
def switch(cnt):
    global maxN
    if cnt == int(t):
        rlt = int(''.join(nums))
        if rlt > maxN:
            maxN = rlt
        return
 
    elif 1 <= cnt <= l - 2 and nums[:cnt] != sorted(nums[:cnt], reverse=True):
        return
 
    else:
        for i in range(l-1):
            for j in range(i+1, l):
                nums[i], nums[j] = nums[j], nums[i]
 
                if l >= 3 and nums[0] != max(nums):  # 최댓값이 아니면 pass
                    print(nums)
                    pass
                else:
                    switch(cnt+1)
                nums[i], nums[j] = nums[j], nums[i]
 
# 2
T = int(input())
 
for tc in range(1, T + 1):
 
    nums, t = input().split()
    nums = list(nums)
    print(nums)
    l = len(nums)
 
    maxN = 0
    switch(0)
 
    print(f'#{tc} {maxN}')