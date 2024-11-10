class Solution:
    def knapSack(self, N, W, val, wt):
        # code here
        
        dp = [[0]*(W+1) for _ in range(N+1)]
        
        for i in range(1, N+1):
            for j in range(1, W+1):
                ## we don't take the current item
                dp[i][j] = dp[i-1][j]
                
                if wt[i-1] <= j:
                    dp[i][j] = max(dp[i][j], val[i-1] + dp[i][j - wt[i-1]])
                    
                    
        return dp[N][W]