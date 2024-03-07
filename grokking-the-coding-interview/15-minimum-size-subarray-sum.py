import sys
def min_sub_array_len(target, nums):

    # Replace this placeholder return statement with your code
    minimum_length = sys.maxsize
    curr_sum = 0
    length = 0
    start = 0
    for i in range(len(nums)):
        curr_sum = curr_sum + nums[i]
        
        if curr_sum >= target:
            while curr_sum >= target:
                length = i - start + 1
                if length < minimum_length:
                    minimum_length = length

                curr_sum = curr_sum - nums[start]
                start +=1
                

    if minimum_length == sys.maxsize:
        return 0


    return minimum_length