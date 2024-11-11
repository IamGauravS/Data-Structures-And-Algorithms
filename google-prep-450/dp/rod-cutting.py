class Solution:
    def cutRod(self, price, n):
        # dp[j] will store the maximum profit for a rod of length `j`
        dp = [0] * (n + 1)
        
        # For each piece length `i`, update dp array for all lengths `j`
        for i in range(1, n + 1):
            for j in range(i, n + 1):
                dp[j] = max(dp[j], price[i - 1] + dp[j - i])
        
        return dp[n]
