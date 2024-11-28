#
# @lc app=leetcode id=554 lang=python3
#
# [554] Brick Wall
#

# @lc code=start
from collections import defaultdict
class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        
        width = sum(wall[0])

        if width == 1:
            return len(wall)

        minCrosses = float('inf')

        edgeCount = defaultdict(int)

        
        for layer in wall:
                prev = layer[0]
                for i in range(1, len(layer)):
                    edgeCount[prev] += 1
                    prev += layer[i]

        if len(edgeCount) == 0:
            return len(wall)

        return len(wall) - max(edgeCount.values())

        
# @lc code=end

