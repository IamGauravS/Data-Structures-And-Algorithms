class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        noOfCoins = len(coins)
        dp = [[float('inf') for i in range(amount+1)] for j in range(noOfCoins+1)]

        for i in range(noOfCoins+1):
            dp[i][0] = 0

        for i in range(1, noOfCoins+1):
            for j in range(1, amount+1):
                if coins[i-1] <= j:  ## value of coin is less then amount then only we can consider it
                    dp[i][j] = min(dp[i-1][j], 1+ dp[i][j-coins[i-1]])

                else:
                    dp[i][j] = dp[i-1][j]


        return dp[noOfCoins][amount] if dp[noOfCoins][amount] != float('inf') else -1

## optimised solution
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        max_val = amount + 1
        dp = [max_val] * (amount + 1)
        dp[0] = 0

        for coin in coins:  ## we run a double loop and we only consider coins above or equal to coin value
            for i in range(coin, amount + 1):
                dp[i] = min(dp[i], dp[i - coin] + 1)

        return dp[amount] if dp[amount] != max_val else -1

