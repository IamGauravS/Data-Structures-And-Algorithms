#
# @lc app=leetcode id=994 lang=python3
#
# [994] Rotting Oranges
#

# @lc code=start
from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        queue = deque()
        rows, cols = len(grid), len(grid[0])
        freshOranges = 0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    queue.append((i, j))
                if grid[i][j] == 1:
                    freshOranges += 1

        delta = [(1,0), (-1,0), (0,-1), (0,1)]

        noOfMinute = 0
        while queue and freshOranges:
            queueLen = len(queue)
            noOfMinute += 1

            for _ in range(queueLen):
                curri, currj = queue.popleft()
                for dx, dy in delta:
                    if 0 <= curri + dx < rows and 0 <= currj + dy < cols and grid[curri+dx][currj+dy] == 1:
                        grid[curri+dx][currj+dy] = 2
                        queue.append((curri+dx, currj+dy))
                        freshOranges -= 1


        if freshOranges == 0:
            return noOfMinute 
        return -1

        
# @lc code=end

