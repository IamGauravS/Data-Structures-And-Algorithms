#
# @lc app=leetcode id=123 lang=python3
#
# [123] Best Time to Buy and Sell Stock III
#

# @lc code=start
class Solution:
    def maxProfitHelper(self, index, prices, currTrade):
        if index == len(prices) or currTrade == 5:
            return 0
        if (index, currTrade) in self.memoryDict:
            return self.memoryDict[(index, currTrade)]
        
        ## buy condition
        if currTrade % 2 == 0:
            profit = max(self.maxProfitHelper(index+1, prices, currTrade), -prices[index] + self.maxProfitHelper(index+1, prices, currTrade+1))

        else:
            profit = max(self.maxProfitHelper(index+1, prices, currTrade), prices[index] + self.maxProfitHelper(index+1, prices, currTrade+1))

        return profit
    
    
    def maxProfitHelperDP(self, prices):
        n = len(prices)
        # Initialize DP table: (n+1) x 2 x 3
        # dp[ind][buy][cap] represents the maximum profit from day 'ind' with 'buy' state and 'cap' transactions left
        dp = [[[0 for _ in range(3)] for _ in range(2)] for _ in range(n + 1)]

        # Iterate from the last day to the first day
        for ind in range(n - 1, -1, -1):
            for buy in range(2):
                for cap in range(1, 3):  # cap = 1 or 2
                    if buy == 1:
                        # Option 1: Do not buy on day 'ind'
                        # Option 2: Buy on day 'ind' and move to sell state without changing 'cap'
                        dp[ind][buy][cap] = max(
                            dp[ind + 1][buy][cap], 
                            -prices[ind] + dp[ind + 1][0][cap]
                        )
                    else:
                        # Option 1: Do not sell on day 'ind'
                        # Option 2: Sell on day 'ind' and decrement 'cap' by 1
                        dp[ind][buy][cap] = max(
                            dp[ind + 1][buy][cap], 
                            prices[ind] + dp[ind + 1][1][cap - 1] ## we decrease cap here bcoz we have less transactons left
                        )

        # The result is the maximum profit starting from day 0, with the ability to buy, and having 2 transactions left
        return dp[0][1][2]
    
    
    def maxProfitHelperDPV2(self, prices):
        n = len(prices)
        
        # Initializing two states (current and next day) for each transaction state
        dp_next = [[0] * 3 for _ in range(2)]  # `buy/sell` states for the next day
        dp_current = [[0] * 3 for _ in range(2)]  # `buy/sell` states for the current day
        
        for ind in range(n - 1, -1, -1):
            for cap in range(1, 3):
                # If we are in a "buy" state, either we buy or skip to next day
                dp_current[1][cap] = max(dp_next[1][cap], -prices[ind] + dp_next[0][cap])
                
                # If we are in a "sell" state, either we sell or skip to next day
                dp_current[0][cap] = max(dp_next[0][cap], prices[ind] + dp_next[1][cap - 1])
            
            # Move current day's results to next day's state
            dp_next = [row[:] for row in dp_current]

        return dp_next[1][2]

        
    def maxProfit(self, prices: List[int]) -> int:
        self.memoryDict = {}

        return self.maxProfitHelperDPV2(prices)
        
# @lc code=end

