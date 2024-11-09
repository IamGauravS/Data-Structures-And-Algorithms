class Solution:
    def topDownDp(self, i, arr, sum):
        if sum == 0:
            return True 
        if i >= len(arr):
            return False 
        
        if (i, sum) in self.memoDict:
            return self.memoDict[(i, sum)]
        
        if arr[i] <= sum:
            self.memoDict[(i, sum)] = self.topDownDp(i+1, arr, sum-arr[i]) or self.topDownDp(i+1, arr, sum)
        else:
            self.memoDict[(i, sum)] = self.topDownDp(i+1, arr, sum)

        return self.memoDict[(i, sum)] 
    
    def isSubsetSum(self, arr, sum):
        self.memoDict = {}
        return self.topDownDp(0, arr, sum)


## bottoms up approach

class Solution:
    def isSubsetSum(self, arr: List[int], sum: int) -> bool:
        n = len(arr)
        
        # Create a DP table with (n+1) rows and (sum+1) columns
        dp = [[False] * (sum + 1) for _ in range(n + 1)]
        
        # Base Case: A subset sum of 0 is always possible with an empty subset
        for i in range(n + 1):
            dp[i][0] = True
        
        # Fill the DP table
        for i in range(1, n + 1):
            for j in range(1, sum + 1):
                # Exclude the current element
                dp[i][j] = dp[i-1][j]
                
                # Include the current element if it does not exceed the sum
                if arr[i-1] <= j:
                    dp[i][j] = dp[i][j] or dp[i-1][j - arr[i-1]]
        
        # The answer will be in the last cell
        return dp[n][sum]

