def find_sum_of_three(nums, target):
   # Replace this placeholder return statement with your code
   nums = sorted(nums)
   n = len(nums)

   for i in range(n):
      low = i+1
      high = n-1
      while low < high:
         s = nums[low] + nums[i] + nums[high]
         if s == target:
            return True 
         elif s > target:
            high -=1
         else :
            low += 1
   return False


## the logic is that once we fix one number then it just becomes like a two pointer