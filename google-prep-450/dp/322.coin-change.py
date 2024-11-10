#
# @lc app=leetcode id=322 lang=python3
#
# [322] Coin Change
#

# @lc code=start
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [[float('inf')]*(amount+1) for _ in range(len(coins)+1)]

        for i in range(len(coins) + 1):
            dp[i][0] = 0

        for i in range(1, len(coins)+1):
            for j in range(1, amount+1):

                ## do not consider this coin
                dp[i][j] = dp[i-1][j]

                ## consider this coin
                if coins[i-1] <= j:
                    dp[i][j] = min(dp[i][j], dp[i][j - coins[i-1]] + 1)

        return dp[len(coins)][amount] if dp[len(coins)][amount] != float('inf') else -1


        
# @lc code=end

