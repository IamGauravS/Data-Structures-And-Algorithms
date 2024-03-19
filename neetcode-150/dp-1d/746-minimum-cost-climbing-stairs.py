class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        if len(cost) == 1:
            return cost[0]
        
        dp_cost = [0 for i in range(len(cost)+2)]
        
        dp_cost[1] = 0
        dp_cost[2] = 0
        
        for i in range(3, len(cost)+2):
            dp_cost[i] = min(dp_cost[i-1] + cost[i-2], dp_cost[i-2] + cost[i-3])
            
            
        return dp_cost[-1]
            
        
        
        