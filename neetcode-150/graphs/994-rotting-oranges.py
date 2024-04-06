import queue
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rootenOrangeQueue = queue.Queue()
        noFreshOranges = 0
        self.grid = grid 
        
        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                if self.grid[i][j] == 2:
                     rootenOrangeQueue.put([0, i,j])  ## time, i, j
                if self.grid[i][j] == 1:
                    noFreshOranges += 1
                    
        if noFreshOranges == 0:
            return 0
         
        maxTime = 0
        while not rootenOrangeQueue.empty():
            currTime, curri, currj = rootenOrangeQueue.get()
            maxTime = max(maxTime, currTime)
            
            delta = [(0,1), (0,-1), (1,0), (-1,0)]
            for dx, dy in delta:
                nexti = curri + dx 
                nextj = currj + dy 
                
                if 0 <= nexti < len(self.grid) and 0 <= nextj < len(self.grid[0]) and self.grid[nexti][nextj] == 1:
                    noFreshOranges -= 1
                    self.grid[nexti][nextj] = 2
                    rootenOrangeQueue.put([currTime+1, nexti, nextj])
                    
                    
        if noFreshOranges == 0:
            return maxTime
        
        else:
            return -1
                            