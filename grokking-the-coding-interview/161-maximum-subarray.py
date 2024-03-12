import sys 
def max_sub_array(nums):
  
    if len(nums) ==0:
        return -1

    max_sum = -sys.maxsize - 1
    curr_sum = 0
    for num in nums:
        curr_sum = max(num, curr_sum + num)
        max_sum = max(max_sum, curr_sum)
            
    return max_sum