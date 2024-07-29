class Solution:
    def findMinTime(self, currLoc):
        curri = currLoc[0]
        currj = currLoc[1]
        
        if curri == len(self.grid)-1 and currj == len(self.grid[0])-1:
            return self.grid[curri][currj]
        
        if self.dp[curri][currj] != float('inf'):
            return self.dp[curri][currj]
        
        pathMin = float('inf')
        delta = [(0,1), (0,-1), (1,0), (-1,0)]
        
        for dx, dy in delta:
            nexti = curri+dx
            nextj = currj+dy 
            if 0 <= nexti < len(self.grid) and 0 <= nextj < len(self.grid[0])  and self.visited[nexti][nextj] == False:
                self.visited[nexti][nextj] = True 
                pathMin = min(self.findMinTime((nexti, nextj)), pathMin)
                self.visited[nexti][nextj] = False 
            
        self.dp[curri][currj] = max(pathMin, self.grid[curri][currj])
        return self.dp[curri][currj]
            
    def swimInWater(self, grid: List[List[int]]) -> int:
        self.grid = grid 
        
        self.visited = [[False for j in range(len(self.grid[0]))] for i in range(len(self.grid))]
        self.dp = [[float('inf') for j in range(len(self.grid[0]))] for i in range(len(self.grid))]
        
        
        self.visited[0][0] = True 
        self.dp[0][0] = self.findMinTime((0,0))
        return self.dp[0][0]
    
    
    
###  DP is sort of based on precomputation, in which current state depends on the states which have already been 
# computed. DP will not work in this problem because, the current state will depend not only on the states which
# have been computed but also on the states which will be computed in the future.
##For instance, if from a given a cell only right and bottom moves were allowed, then the state for the current 
# cell depends on the right and bottom cells only. But here it depends on the top and left cells as well. Now for
# those the top and left cells this current cell acts as bottom and right cell respectively. So you see there is a 
# circular dependency which will not be resolved if we use DP


import heapq
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        visited = set()
        heap = []
        self.grid = grid 
        
        heapq.heappush(heap, (self.grid[0][0], 0, 0))  ## time, i, j
        
        while heap:
            time, curri, currj = heapq.heappop(heap)
            if curri == len(self.grid)-1 and currj == len(self.grid[0])-1:
                return time 
            
            visited.add((curri, currj))
            delta = [(0,1), (0,-1), (-1,0), (1,0)]
            
            for dx, dy in delta:
                nexti = curri+dx 
                nextj = currj+dy 
                
                if 0 <= nexti < len(self.grid) and 0 <= nextj < len(self.grid[0]) and (nexti, nextj) not in visited:
                    visited.add((nexti, nextj))
                    heapq.heappush(heap, (max(self.grid[nexti][nextj], time), nexti, nextj))
                    
                    
        