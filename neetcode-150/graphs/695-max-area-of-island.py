class Solution:
    def calculateArea(self, curri, currj):
        if self.grid[curri][currj] == 0:
            return 0
        
        currArea = 1
        
        self.grid[curri][currj] = 0
        
        delta = [(0,1), (0,-1), (-1,0), (1,0)]
        
        for dx, dy in delta:
            nexti = curri + dx
            nextj = currj + dy 
            
            if 0 <= nexti < len(self.grid) and 0 <= nextj < len(self.grid[0]) and self.grid[nexti][nextj] == 1:
                currArea += self.calculateArea(nexti, nextj)
                
        return currArea
    
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxAreaOfIsland = 0
        
        self.grid = grid 
        
        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                if self.grid[i][j] == 1:
                    area = self.calculateArea(i, j)
                    maxAreaOfIsland = max(area, maxAreaOfIsland)
                    
        return maxAreaOfIsland
        