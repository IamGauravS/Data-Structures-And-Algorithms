import queue

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        max_time = 0
        
        height = len(grid)
        width = len(grid[0])
        no_of_fresh_oranges = 0
        q = queue.Queue()
        
        for i in range(height):
            for j in range(width):
                if grid[i][j] == 2:
                    q.put((0, i, j))
                elif grid[i][j] ==1:
                    no_of_fresh_oranges +=1
                    
        while not q.empty():
            curr_time, i, j = q.get()
            if curr_time > max_time:
                max_time = curr_time
                
            
            
            delta = [(0,1), (1,0), (0,-1), (-1,0)]
            
            for dx, dy in delta:
                newi = dx + i 
                newj = dy + j 
                
                if 0 <= newi < height and 0 <= newj < width and grid[newi][newj] == 1 :
                    q.put((curr_time+1, newi, newj))
                    no_of_fresh_oranges -=1
                    grid[newi][newj] = 2
                    
        
        return -1 if no_of_fresh_oranges > 0 else max_time    
            