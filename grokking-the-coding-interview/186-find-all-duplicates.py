def find_duplicates(nums):
  
    # Replace this placeholder return statement with your code
    for i in range(len(nums)):
        while nums[i] != nums[nums[i]-1]:
            nums[nums[i]-1], nums[i] = nums[i], nums[nums[i]-1]
            
            
    duplicates = []
    for i in range(len(nums)):
        if nums[i] != i+1:
            duplicates.append(nums[i])
            
    return duplicates
