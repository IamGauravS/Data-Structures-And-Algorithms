#
# @lc app=leetcode id=494 lang=python3
#
# [494] Target Sum
#

# @lc code=start

from typing import List

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        totalSum = sum(nums)
        
        # If target is impossible to achieve with the given nums
        if abs(target) > totalSum:
            return 0
        
        offset = totalSum  # Offset to shift indices for handling negative sums
        dp = [[0] * (2 * totalSum + 1) for _ in range(len(nums) + 1)]
        dp[0][offset] = 1  # Start with sum = 0 at index 0
        
        for i in range(1, len(nums) + 1):
            for j in range(-totalSum, totalSum + 1):
                if dp[i - 1][j + offset] > 0:  # If there's a way to achieve this sum with i-1 elements
                    dp[i][j + nums[i - 1] + offset] += dp[i - 1][j + offset]  # Add nums[i - 1]
                    dp[i][j - nums[i - 1] + offset] += dp[i - 1][j + offset]  # Subtract nums[i - 1]
        
        # Target sum ways will be found at dp[len(nums)][target + offset]
        return dp[len(nums)][target + offset] if -totalSum <= target <= totalSum else 0

        
# @lc code=end

