#
# @lc app=leetcode id=188 lang=python3
#
# [188] Best Time to Buy and Sell Stock IV
#

# @lc code=start
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if not prices:
            return 0
        
        dp = [[[0]*(k+1) for _ in range(2)] for _ in range(len(prices)+1)]

        for day in range(len(prices)-1, -1, -1):
            for trans in range(2):
                for cap in range(1,k+1):
                    if trans:
                        dp[day][trans][cap] = max(dp[day+1][trans][cap], -prices[day] + dp[day+1][0][cap])
                    else:
                        dp[day][trans][cap] = max(dp[day+1][trans][cap], prices[day] + dp[day+1][1][cap-1])

        return dp[0][1][k]
        
# @lc code=end

