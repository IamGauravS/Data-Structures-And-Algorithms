class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ## if buy -> i+1
        ## if sell -> i+2

        dp = {}  ## key=(i, buying) val = maxProfit

        def dfs(i, buying):
            if i>= len(prices): ## we do greater to bcoz we can go out of bounds too
                return 0

            if (i, buying) in dp:
                return dp[(i, buying)]

            if buying:
                buy = dfs(i+1, not buying) - prices[i]
                cooldown = dfs(i+1, buying)
                dp[(i, buying)] = max(buy, cooldown)
            else:
                sell = dfs(i+2, not buying) + prices[i]  ## if we sell cooldown period is there
                cooldown = dfs(i+1, buying)
                dp[(i, buying)] = max(sell, cooldown)

            return dp[(i, buying)]


        return dfs(0, True)
            




def stock_profit(prices):
    n = len(prices)
    
    # Create a 2D dp array of size [n+2][2] initialized to 0
    dp = [[0 for _ in range(2)] for _ in range(n + 2)]

    for ind in range(n - 1, -1, -1):
        for buy in range(2):
            profit = 0

            if buy == 0:  # We can buy the stock
                profit = max(
                    0 + dp[ind + 1][0],
                    -prices[ind] + dp[ind + 1][1]
                )

            if buy == 1:  # We can sell the stock
                profit = max(
                    0 + dp[ind + 1][1],
                    prices[ind] + dp[ind + 2][0]
                )

            dp[ind][buy] = profit

    return dp[0][0]


if __name__ == "__main__":
    prices = [4, 9, 0, 4, 10]

    result = stock_profit(prices)
    print(f"The maximum profit that can be generated is {result}")


