#
# @lc app=leetcode id=312 lang=python3
#
# [312] Burst Balloons
#

# @lc code=start
class Solution:
    def maxCoinsHelper(self, nums, start, end):
        if start > end:
            return 0

        if (start, end) in self.memoryDict:
            return self.memoryDict[(start, end)]
        

        maxCoins = -float('inf')
        for i in range(start, end+1):
            coin = nums[start-1]*nums[i]*nums[end+1] + self.maxCoinsHelper(nums, start ,i-1) + self.maxCoinsHelper(nums, i+1, end)
            maxCoins = max(maxCoins, coin)

        self.memoryDict[(start, end)] = maxCoins
        return self.memoryDict[(start, end)]


    def maxCoins(self, nums: List[int]) -> int:
        
        nums = [1] + nums + [1]
        dp = [[0]*len(nums) for _ in range(len(nums))]

        for i in range(len(nums)-2, 0, -1):
            for j in range(i, len(nums)-1):
                start = i
                end = j
                maxCoins = -float('inf')
                for ind in range(start, end+1):
                    maxCoins = max(maxCoins, nums[start-1]*nums[ind]*nums[end+1] + dp[start][ind-1] + dp[ind+1][end])

                dp[i][j] = maxCoins
        return dp[1][len(nums)-2]

        

#1. allot last 5 mins for rest of the team
#2. quick time check 
#3.  
        
        
# @lc code=end

