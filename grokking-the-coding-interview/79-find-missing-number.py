def find_missing_number(nums):
  
  # Your code will replace this placeholder return statement
  for i in range(len(nums)):
      
      while nums[i]  != i and nums[i] < len(nums):
          temp = nums[i]
          nums[i] = nums[temp]
          nums[temp] = temp
          
          
  for i, num in enumerate(nums):
            if i != num:
                return i 
            
  return -1