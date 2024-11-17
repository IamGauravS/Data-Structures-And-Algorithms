#
# @lc app=leetcode id=312 lang=python3
#
# [312] Burst Balloons
#

# @lc code=start
class Solution:
    def maxCoinsHelper(self, start, end):
        if start > end:
            return 0 
        if (start, end) in self.memoDict:
            return self.memoDict[(start, end)]
        
        maxCoins = -float('inf')

        for ind in range(start, end+1):
            coins = self.nums[start-1]*self.nums[ind]*self.nums[end+1] + self.maxCoinsHelper(start, ind-1) + self.maxCoinsHelper(ind+1, end)
            maxCoins = max(coins, maxCoins)

        self.memoDict[(start, end)] = maxCoins
        return self.memoDict[(start, end)]

        
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        dp = [[0]*len(nums) for _ in range(len(nums))]

        for i in range(len(nums)-2, 0, -1):
            for j in range(i, len(nums)-1):
                start = i
                end = j 

                maxCoins = -float('inf')

                for ind in range(start, end+1):
                    coins = nums[start-1]*nums[ind]*nums[end+1] + dp[start][ind-1] + dp[ind+1][end]
                    maxCoins = max(coins, maxCoins)


                dp[i][j] = maxCoins

        return dp[1][len(nums)-2]



    # def maxCoins(self, nums: List[int]) -> int:
    #     nums = [1] + nums + [1]
    #     self.nums = nums 
    #     self.memoDict = {}
    #     return self.maxCoinsHelper(1, len(nums)-2)
        
# @lc code=end

