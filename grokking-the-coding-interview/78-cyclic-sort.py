def implement_cyclic_sort(nums):
    
    for i in range(len(nums)):
        while nums[i] != i+1:
            nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
            
            
    return nums 