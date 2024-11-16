#
# @lc app=leetcode id=309 lang=python3
#
# [309] Best Time to Buy and Sell Stock with Cooldown
#

# @lc code=start
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        n = len(prices)
        dp_next = [0, 0]  # dp[i+1]
        dp_next_next = [0, 0]  # dp[i+2]

        for i in range(n - 1, -1, -1):
            dp_curr = [0, 0]  # dp[i]
            dp_curr[1] = max(dp_next[1], -prices[i] + dp_next[0])  # Holding a stock
            dp_curr[0] = max(dp_next[0], prices[i] + dp_next_next[1])  # Not holding a stock
            dp_next_next = dp_next
            dp_next = dp_curr

        return dp_next[1]





        
# @lc code=end

