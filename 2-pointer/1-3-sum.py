

def find_3_sum(nums, target):
    output = []
    frequency_map = {}
    for num in nums:
        if num not in frequency_map:
            frequency_map[num] = 0
        frequency_map[num] += 1
        
    for i in range(len(nums)):
        a = nums[i]
        frequency_map[a] -=1
        for j in range(i+1, len(nums)):
            b= nums[j]
            frequency_map[b] -= 1
            value_required = target - (a+b)
            if value_required in frequency_map and frequency_map[value_required] > 0:
                output.append([a,b,value_required])
            
            frequency_map[b] +=1
            
        frequency_map[a] +=1
        
        
    return output
        
   
   
## this handles duplicates as we only want unique triplets
## we start with one element and then use two pointer to find other two elements     
        
def find_3_sum(nums, target):
    output = []
    nums.sort()  # Sort the input list to handle duplicates properly
    n = len(nums)
    
    for i in range(n - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue  # Skip duplicate elements
        
        left = i + 1
        right = n - 1
        
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            if total == target:
                output.append([nums[i], nums[left], nums[right]])
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

    