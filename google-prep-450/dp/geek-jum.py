class Solution:
    def minimumEnergy(self, height, n):
        # Code here
        if n <= 1:
            return 0
            
        if n == 2:
            return abs(height[0]-height[1])
            
        prevprevCost = 0
        prevCost = abs(height[0] - height[1])
        currCost = 0
        
        for i in range(2, n):
            currCost = min(prevCost + abs(height[i] - height[i-1]), prevprevCost + abs(height[i] - height[i-2]))
            
            prevprevCost, prevCost = prevCost, currCost
            
        return currCost