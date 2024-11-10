from typing import List

class Solution:
    def perfectSum(self, arr: List[int], n: int, target_sum: int) -> int:
        # Define the modulo for large results
        MOD = 10**9 + 7
        
        # Initialize the dp array with zeros
        dp = [[0] * (target_sum + 1) for _ in range(n + 1)]
        
        # Base case: There's 1 way to achieve sum 0 with zero elements (do nothing)
        dp[0][0] = 1
        
        # Fill the dp table
        for i in range(1, n + 1):
            for j in range(target_sum + 1):
                # Exclude the current element
                dp[i][j] = dp[i - 1][j]
                
                # Include the current element if it does not exceed the current sum
                if arr[i - 1] <= j:
                    dp[i][j] = (dp[i][j] + dp[i - 1][j - arr[i - 1]]) % MOD
        
        # The result is the number of ways to achieve the target sum with all elements considered
        return dp[n][target_sum]



class Solution:
    def memoization(self, index, arr, currSum, target):
        
        if index == len(arr):
            if currSum == target:
                return 1
            else:
                return 0
        
        if (index, currSum) in self.memory:
            return self.memory[(index, currSum)]
            
        ## dont include
        self.memory[(index, currSum)] = self.memoization(index+1, arr, currSum, target)
        
        ## include
        if currSum + arr[index] <= target:
            self.memory[(index, currSum)] += self.memoization(index + 1, arr, currSum + arr[index], target)
            
        
        return self.memory[(index, currSum)]
        
    def perfectSum(self, arr, n, sum):
        # code here
        self.memory = {}
		
        return self.memoization(0, arr, 0, sum)%(10**9+7)