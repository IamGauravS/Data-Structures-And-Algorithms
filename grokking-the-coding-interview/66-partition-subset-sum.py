


def can_partition_array(nums):
    
    # Replace this placeholder return statement with your code
    
    total_sum = sum(nums)
    if total_sum % 2 != 0:
        return False 
    
    target = total_sum//2
    nums = sorted(nums)
    dp = [[False for i in range(target+1)] for j in range(len(nums)+1)]
    dp[0][0] = True
    
    for i in range(1, len(nums)+1):
        for j in range(1, target+1):
            curr_val = nums[i-1]
            if j >= curr_val:
                prev_val = dp[i-1][j-curr_val] or dp[i-1][j]
                dp[i][j] = prev_val
            else:
                dp[i][j] = dp[i-1][j]
            
            
    for i in range(len(nums)+1):
        if dp[i][target] == True:
            return True 
        
    else:
        return False 
            
## If you remove this line, dp[i][j] will remain False (its initial value) when nums[i-1] > j, which is not correct. It's possible that you can make up the current sum using some of the previous numbers, even if you can't use the current number.