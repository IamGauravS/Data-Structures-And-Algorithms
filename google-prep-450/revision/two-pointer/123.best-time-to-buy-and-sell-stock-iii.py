#
# @lc app=leetcode id=123 lang=python3
#
# [123] Best Time to Buy and Sell Stock III
#

# @lc code=start
class Solution:
    def maxProfitHelper(self, prices, ind, buy, cap):
        # Base case: End of array or maximum transactions reached
        if ind == len(prices) or cap == 0:
            return 0

        if (ind, buy, cap) in self.memDict:
            return self.memDict[(ind, buy, cap)]

        skip = self.maxProfitHelper(prices, ind+1, buy, cap)
        if buy:
            transaction = -prices[ind] + self.maxProfitHelper(prices, ind+1, 0, cap)
        else:
            transaction = prices[ind] + self.maxProfitHelper(prices, ind+1, 1, cap-1)

        self.memDict[(ind, buy, cap)] =  max(skip, transaction)
        return self.memDict[(ind, buy, cap)]


    def maxProfit(self, prices: List[int]) -> int:
        # Number of days and transactions
        n = len(prices)
        maxTransactions = 2

        # Initialize DP table
        dp = [[[0] * (maxTransactions + 1) for _ in range(2)] for _ in range(n + 1)]

        # Bottom-up calculation
        for ind in range(n - 1, -1, -1):  # Loop over days
            for cap in range(1, maxTransactions + 1):  # Loop over transaction capacity
                for buy in range(2):  # Loop over buy/sell state (0 or 1)
                    if buy:
                        dp[ind][buy][cap] = max(dp[ind + 1][buy][cap], -prices[ind] + dp[ind + 1][0][cap])
                    else:
                        dp[ind][buy][cap] = max(dp[ind + 1][buy][cap], prices[ind] + dp[ind + 1][1][cap - 1])

        # Result: Start from day 0, with buying allowed and max capacity
        return dp[0][1][maxTransactions]

        

        
# @lc code=end

