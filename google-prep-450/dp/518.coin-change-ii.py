#
# @lc app=leetcode id=518 lang=python3
#
# [518] Coin Change II
#

# @lc code=start
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [[0]*(amount+1) for _ in range(len(coins)+1)]

        ## 1 way to make amount 0 we do not take any coin
        for i in range(len(coins) + 1):
            dp[i][0] = 1

        for i in range(1, len(coins)+1):
            for j in range(1, amount+1):
                dp[i][j] = dp[i-1][j]

                if coins[i-1] <= j:
                    dp[i][j] += dp[i][j-coins[i-1]]

        return dp[len(coins)][amount]
        
# @lc code=end

