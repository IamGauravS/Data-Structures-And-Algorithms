import queue

class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        height = len(rooms)
        width = len(rooms[0])
        
        q = queue.Queue()
        
        for i in range(height):
            for j in range(width):
                if rooms[i][j] == 0:
                    q.put((0, i, j))
                    
                    
        while not q.empty():
            dist, i, j = q.get()
            
            delta = [(0,1), (-1,0), (0,-1), (1,0)]
            
            for dx, dy in delta:
                newi = i+dx 
                newj = j+dy 
                
                if 0 <= newi < height and 0 <= newj < width and rooms[newi][newj] != -1:
                    if rooms[newi][newj] > dist + 1:
                        rooms[newi][newj] = dist + 1
                        q.put((dist+1, newi, newj))

        return rooms                    
        
        