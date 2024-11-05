#
# @lc app=leetcode id=1091 lang=python3
#
# [1091] Shortest Path in Binary Matrix
#

# @lc code=start
from collections import deque
from typing import List

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        # If start or end is blocked, return -1 immediately
        if not grid or grid[0][0] != 0 or grid[-1][-1] != 0:
            return -1

        nrows, ncols = len(grid), len(grid[0])
        queue = deque([(0, 0)])
        grid[0][0] = 1  # Mark as visited by setting it to the path length

        # All possible 8 directions
        delta = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, 1), (1, -1), (-1, -1)]
        
        while queue:
            x, y = queue.popleft()
            # If we reach the bottom-right cell, return its distance value
            if (x, y) == (nrows - 1, ncols - 1):
                return grid[x][y]

            for dx, dy in delta:
                nx, ny = x + dx, y + dy
                # Check if (nx, ny) is within bounds and is not yet visited (value is 0)
                if 0 <= nx < nrows and 0 <= ny < ncols and grid[nx][ny] == 0:
                    queue.append((nx, ny))
                    grid[nx][ny] = grid[x][y] + 1  # Set path length at this cell

        return -1  # If no path exists



# @lc code=end

