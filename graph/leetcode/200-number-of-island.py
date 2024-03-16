class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        no_of_island = 0
        
        visited = [[False for i in range(len(grid[0]))] for j in range(len(grid))]
        
        for i in range(len(grid)):
            for j in range(len(grid)):
                if grid[i][j] == "1" and visited[i][j] == False:
                    no_of_island +=1 
                    self.dfs(grid, visited, (i,j))
                    
        return no_of_island
    
    
    def dfs(self, grid, visited, src):
        i, j = src
        if visited[i][j] == True:
            return 
        visited[i][j] = True 
        
        delta = [(1,0), (-1,0), (0,-1), (0,1)]
        
        for dx, dy in delta:
            newi = i+dx 
            newj = j+dy 
            if 0 <= newi < len(grid) and 0 <= newj < len(grid) and grid[newi][newj] == "1":
                self.dfs(grid, visited, (newi, newj))
                
        return 