#
# @lc app=leetcode id=714 lang=python3
#
# [714] Best Time to Buy and Sell Stock with Transaction Fee
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        dp = [[0]*2 for _ in range(len(prices)+1)]

        for i in range(len(prices)-1, -1, -1):
            for state in range(2):
                if state:
                    dp[i][state] = max(dp[i+1][state], -prices[i] + dp[i+1][0])
                else:
                    dp[i][state] = max(dp[i+1][state], prices[i] + dp[i+1][1]-fee)

        return dp[0][1]
        
# @lc code=end

