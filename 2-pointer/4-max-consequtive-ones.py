

def max_consecutive_ones(nums):
    count = 0
    maximum = 0
    
    for i in range(len(nums)):
        if nums[i] == 1:
            count +=1
        else:
            if count > maximum:
                maximum = count 
            count =0
            
    maximum = max(count, maximum)
    return maximum