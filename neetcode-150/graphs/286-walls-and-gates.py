import queue
class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        self.rooms = rooms
        distanceQueue = queue.Queue()
        
        for i in range(len(self.rooms)):
            for j in range(len(self.rooms[0])):
                if rooms[i][j] == 0:
                    distanceQueue.put((0, i, j))  ## distance, i, j
                    
        while not distanceQueue.empty():
            currDistance, curri, currj = distanceQueue.get()
            
            delta = [(0,1), (-1,0), (1,0), (0,-1)]
            
            for dx, dy in delta:
                nexti = curri + dx 
                nextj = currj + dy 
                
                if 0 <= nexti < len(self.rooms) and 0 <= nextj < len(self.rooms[0]) and self.rooms[nexti][nextj] == 2147483647:
                    self.rooms[nexti][nextj] = currDistance + 1 
                    distanceQueue.put((currDistance+1, nexti, nextj))
                    
        return self.rooms 
        