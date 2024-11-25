#
# @lc app=leetcode id=309 lang=python3
#
# [309] Best Time to Buy and Sell Stock with Cooldown
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0
        
        dp = [[0]*2 for _ in range(len(prices) + 2)]

        for i in range(len(prices)-1, -1, -1):
            for state in range(2):
                if state:
                    dp[i][state] = max(dp[i+1][state], -prices[i] + dp[i+1][0])
                else:
                    dp[i][state] = max(dp[i+1][state], prices[i] + dp[i+2][1])

        return dp[0][1]
        
# @lc code=end

