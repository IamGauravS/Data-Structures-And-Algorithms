class Solution:
    def isSubsetSum(self, arr, target):
        # Handle edge cases
        if target > sum(arr):
            return False
        
        # Initialize the DP table
        dp = [[False] * (target + 1) for _ in range(len(arr) + 1)]
        
        # Base case: Sum of 0 is always possible (empty subset)
        for i in range(len(arr) + 1):
            dp[i][0] = True
        
        # Fill the DP table
        for i in range(1, len(arr) + 1):
            for j in range(1, target + 1):
                if j >= arr[i - 1]:  # Include the current element
                    dp[i][j] = dp[i - 1][j] or dp[i - 1][j - arr[i - 1]]
                else:  # Exclude the current element
                    dp[i][j] = dp[i - 1][j]
        
        # The result is stored in dp[len(arr)][target]
        return dp[len(arr)][target]
