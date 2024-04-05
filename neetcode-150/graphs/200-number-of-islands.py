class Solution:
    def makeWater(self, curri, currj):
        if self.grid[curri][currj] == '0':
            return 
        
        self.grid[curri][currj] = '0'
        
        delta = [(0,1), (0,-1), (1,0), (-1,0)]
        
        for dx, dy in delta:
            nexti = curri + dx 
            nextj = currj + dy 
            
            if 0 <= nexti < len(self.grid) and 0 <= nextj < len(self.grid[0]) and self.grid[nexti][nextj] == '1':
                self.makeWater(nexti, nextj)
                
        return 
        
    
    def numIslands(self, grid: List[List[str]]) -> int:
        
        self.grid = grid 
        
        
                
        islandCount = 0
        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                if self.grid[i][j] == '1':
                    islandCount += 1
                    self.makeWater(i, j)
                    
        return islandCount
                
                
            