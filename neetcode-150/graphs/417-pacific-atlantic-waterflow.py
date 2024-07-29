class Solution:
    def dfs(self, i, j, visited):
        
        visited.add((i, j))
        
        for dx, dy in [(0,1), (1,0), (0,-1), (-1,0)]:
            newi, newj = i + dx, j + dy
            
            if 0 <= newi < len(self.heights) and 0 <= newj < len(self.heights[0]) and (newi, newj) not in visited and self.heights[newi][newj] >= self.heights[i][j]:
                self.dfs(newi, newj, visited)

    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights: 
            return []
        
        self.heights = heights
        
        m, n = len(heights), len(heights[0])
        
        pacific = set([(i, 0) for i in range(m)] + [(0, j) for j in range(n)])
        
        atlantic = set([(i, n-1) for i in range(m)] + [(m-1, j) for j in range(n)])

        for i, j in list(pacific):
            self.dfs(i, j, pacific)
            
        for i, j in list(atlantic):
            self.dfs(i, j, atlantic)

        return list(pacific & atlantic)