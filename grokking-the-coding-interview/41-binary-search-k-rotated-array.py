def binary_search_rotated(nums, target):
  # Replace this placeholder return statement with your code
  low = 0
  high = len(nums) - 1
  
  while low <= high:
      mid = (low+high)//2 
      
      if nums[mid] == target:
          return mid 
      
      if nums[low] <= nums[mid]:    ## first half is sorted:
          if target < nums[mid] and nums[low] <= target:
              high = mid -1 
          else:
              low = mid +1 
              
      else:
            if target > nums[mid] and target <= nums[high]:
                low = mid+1 
                
            else:
                high = mid -1 
                
                
  return -1
                
            
          
      