class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        stairsCost = [0,0]
        noOfStairs = len(cost)
        for i in range(2, noOfStairs+1):
            currCost = min(stairsCost[i-1] + cost[i-1], stairsCost[i-2] + cost[i-2])
            stairsCost.append(currCost)


        return stairsCost[-1]

        