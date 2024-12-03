#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        prevMax = prices[-1]

        for i in range(len(prices)-2, -1, -1):
            if prevMax > prices[i]:
                profit = max(profit, prevMax - prices[i])
            else:
                prevMax = prices[i]
        return profit
        
# @lc code=end

