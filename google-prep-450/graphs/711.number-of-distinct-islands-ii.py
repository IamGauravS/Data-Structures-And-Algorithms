#
# @lc app=leetcode id=711 lang=python3
#
# [711] Number of Distinct Islands II
#

# @lc code=start
from collections import deque
from typing import List, Tuple

class Solution:
    def findIsland(self, i: int, j: int) -> List[Tuple[int, int]]:
        queue = deque()
        island = []
        queue.append((i, j))
        self.grid[i][j] = '#'
        
        # Define 4-directional movement
        delta = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        
        while queue:
            curri, currj = queue.popleft()
            # Store coordinates relative to starting point
            island.append((curri - i, currj - j))
            
            for dx, dy in delta:
                newi = curri + dx
                newj = currj + dy
                if (0 <= newi < len(self.grid) and 
                    0 <= newj < len(self.grid[0]) and 
                    self.grid[newi][newj] == 1):
                    self.grid[newi][newj] = '#'
                    queue.append((newi, newj))
        return island

    def normalize(self, island: List[Tuple[int, int]]) -> Tuple[Tuple[int, int], ...]:
        # Generate all possible transformations
        candidates = []
        for i in range(8):
            transformed = []
            for x, y in island:
                if i == 0:   # original
                    transformed.append((x, y))
                elif i == 1: # rotate 90
                    transformed.append((-y, x))
                elif i == 2: # rotate 180
                    transformed.append((-x, -y))
                elif i == 3: # rotate 270
                    transformed.append((y, -x))
                elif i == 4: # flip horizontal
                    transformed.append((x, -y))
                elif i == 5: # flip vertical
                    transformed.append((-x, y))
                elif i == 6: # flip diagonal
                    transformed.append((y, x))
                elif i == 7: # flip anti-diagonal
                    transformed.append((-y, -x))
            
            # Normalize to origin
            if transformed:
                min_x = min(x for x, _ in transformed)
                min_y = min(y for _, y in transformed)
                normalized = [(x - min_x, y - min_y) for x, y in transformed]
                normalized.sort()
                candidates.append(tuple(normalized))
        
        # Return the lexicographically smallest transformation
        return min(candidates)

    def numDistinctIslands2(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
            
        self.grid = grid
        islands = set()
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    island = self.findIsland(i, j)
                    normalized_island = self.normalize(island)
                    islands.add(normalized_island)
                    
        return len(islands)
        
# @lc code=end

