#
# @lc app=leetcode id=416 lang=python3
#
# [416] Partition Equal Subset Sum
#

# @lc code=start
class Solution:
    def memoization(self, index, target, nums):
        if target == 0:
            return True 
        if index == len(nums):
            return False
        
        if (target, index) in self.memoryDict:
            return self.memoryDict[(target, index)]
        
        if nums[index] <= target:
            self.memoryDict[(target, index)] = self.memoization(index+1, target - nums[index], nums) or self.memoization(index+1, target, nums)

        else:
            self.memoryDict[(target, index)] = self.memoization(index+1, target, nums)

        return self.memoryDict[(target, index)]
    
    def tabulation(self, nums, target):
        dp = [[False]*(target+1) for _ in range(len(nums)+1)]

        ## since we can always make a subset with sum 0
        n = len(nums)
        for i in range(n+1):
            dp[i][0] = True 

        for i in range(1, n+1):
            for j in range(1, target+1):
                dp[i][j] = dp[i-1][j]

                ## consider the current element
                if nums[i-1] <= j:
                    dp[i][j] = dp[i-1][j] or dp[i-1][j - nums[i-1]]

        return dp[-1][-1]


    
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0:
            return False 
        
        target = sum(nums) // 2

        self.memoryDict = {}
        return self.tabulation(nums, target)
    
        

        
# @lc code=end

