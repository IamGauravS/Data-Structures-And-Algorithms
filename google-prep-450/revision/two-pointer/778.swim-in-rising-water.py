#
# @lc app=leetcode id=778 lang=python3
#
# [778] Swim in Rising Water
#

# @lc code=start
import heapq
from typing import List

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        # Min-heap: (time, x, y)
        heap = [(grid[0][0], 0, 0)]
        visited = [[False] * n for _ in range(n)]
        visited[0][0] = True
        
        while heap:
            time, x, y = heapq.heappop(heap)
            
            # If we reach the bottom-right corner, return the time
            if x == n - 1 and y == n - 1:
                return time
            
            # Explore neighbors
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                    visited[nx][ny] = True
                    heapq.heappush(heap, (max(time, grid[nx][ny]), nx, ny))
        
        return -1  # This line should never be reached


                

        
# @lc code=end

