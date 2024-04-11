class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [0, 0]
        
        n = len(cost)
        for i in range(2,n+1):
            dp.append(min(dp[i-1]+cost[i-1], dp[i-2]+cost[i-2]))
            
        print(dp)
        return dp[-1]
            