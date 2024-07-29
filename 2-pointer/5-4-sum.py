def four_sum(nums, target):
    output = []
    nums.sort()  # Sort the input list to handle duplicates properly
    n = len(nums)
    
    for i in range(n - 3):
        if i > 0 and nums[i] == nums[i - 1]:
            continue  # Skip duplicate elements
        
        for j in range(i + 1, n - 2):
            if j > i + 1 and nums[j] == nums[j - 1]:
                continue  # Skip duplicate elements
            
            left = j + 1
            right = n - 1
            
            while left < right:
                total = nums[i] + nums[j] + nums[left] + nums[right]
                if total == target:
                    output.append([nums[i], nums[j], nums[left], nums[right]])
                    # Move left pointer to next unique element
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    # Move right pointer to next unique element
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif total < target:
                    left += 1
                else:
                    right -= 1
                    
    return output
