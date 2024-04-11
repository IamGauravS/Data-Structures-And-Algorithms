class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        noOfCoins = len(coins)

        dp = [[0 for i in range(amount+1)] for j in range(noOfCoins+1)]
        
        for i in range(noOfCoins+1):
            dp[i][0] = 1 

        for i in range(1, noOfCoins+1):
            for j in range(1, amount+1):
                if coins[i-1] <= j:  ## we can only take if curr value of coin is greater than amount
                    dp[i][j] = dp[i][j-coins[i-1]] 

                dp[i][j] += dp[i-1][j]  ## we can always take from prev


        return dp[noOfCoins][amount]  ## we already consider the prev ones so no need to add everything



## space optimised

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1

        for coin in coins:
            for x in range(coin, amount + 1):
                dp[x] += dp[x - coin]

        return dp[amount]