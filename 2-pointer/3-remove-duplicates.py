def remove_duplicates_from_sorted_array(nums):
    
    i = 0
    
    for j in range(1, len(nums)):
        if nums[i] != nums[j]:
            i+=1
            nums[i], nums[j] = nums[j], nums[i]
            
    return i+1, nums