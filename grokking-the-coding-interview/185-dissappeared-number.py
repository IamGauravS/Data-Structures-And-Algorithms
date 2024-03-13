def find_disappeared_numbers(nums):
    
    for i in range(len(nums)):
        while nums[i] != nums[nums[i] - 1]:
            nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
            
    elements_not_there = []
    for i, num in enumerate(nums):
        if num != i + 1:
            elements_not_there.append(i + 1)
            
    return elements_not_there