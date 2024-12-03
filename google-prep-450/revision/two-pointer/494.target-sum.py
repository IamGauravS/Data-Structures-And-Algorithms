#
# @lc app=leetcode id=494 lang=python3
#
# [494] Target Sum
#

# @lc code=start
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {0: 1}

        for num in nums:
            tempDP = collections.defaultdict(int)
            for sum, count in dp.items():
                tempDP[sum + num] += count
                tempDP[sum - num] += count
            dp = tempDP

        return dp[target]
        
# @lc code=end

