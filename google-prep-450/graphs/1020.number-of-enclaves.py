#
# @lc app=leetcode id=1020 lang=python3
#
# [1020] Number of Enclaves
#

# @lc code=start
from collections import deque
class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        queue = deque()
        visited = set()

        ## add all the corner "O" in the queue
        for r in range(len(grid)):
            if grid[r][0] == 1:
                queue.append((r, 0))
                visited.add((r, 0))
            if grid[r][len(grid[0]) -1] == 1:
                queue.append((r, len(grid[0])-1))
                visited.add((r, len(grid[0])-1))

        for c in range(1, len(grid[0])):
            if grid[0][c] == 1:
                queue.append((0, c))
                visited.add(((0, c)))
            if grid[len(grid) - 1][c] == 1:
                queue.append((len(grid)-1, c))
                visited.add((len(grid)-1, c))

        
        delta = [(1,0), (-1,0), (0,-1), (0,1)]
        while queue:
            curri, currj  = queue.popleft()
            for dx, dy in delta:
                newi = curri + dx 
                newj = currj + dy 

                if 0 <= newi < len(grid) and 0 <= newj < len(grid[0]):
                    if (newi, newj) not in visited and grid[newi][newj] == 1:
                        queue.append((newi, newj))
                        visited.add((newi, newj))

        noOfLandCells = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1 and (r, c) not in visited:
                    noOfLandCells += 1

        return noOfLandCells
# @lc code=end

