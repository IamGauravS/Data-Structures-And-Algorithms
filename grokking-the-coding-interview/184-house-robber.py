import sys 
def rob_houses(nums):

    # Replace this placeholder return statement with your code
    if len(nums) == 1:
        return nums[0]
    
    dp = [nums[0]]
    dp.append(max(nums[0], nums[1]))
    
    for i in range(2, len(nums)):
        dp.append( max(nums[i] + dp[i-2], dp[i-1]))
        
        
    return dp[-1]
