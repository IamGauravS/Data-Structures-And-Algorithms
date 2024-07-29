
import queue
def rotton_oranges(matrix):
    
    ## 0 no orange 1 normal orange 2 rottan orange
    ## find minimum time for all oranges to be rotten
    
    q = queue.Queue()
    
    max_time = 0
    
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 2:
                q.put((i,j, 0))   ## i, j, time
    
    delta = [(0,1), (1,0), (0,-1), (-1,0)]
    
    while not q.empty():
        curr = q.get()
        i, j, time = curr
        if time > max_time:
            max_time = time 
            
        
        for dx, dy in delta:
            if 0 <= i+dx < len(matrix) and 0 <= j+dy < len(matrix[0]) and matrix[i+dx][j+dy] == 1:
                matrix[i+dx][j+dy] = 2
                q.put((i+dx, j+dy, time+1))
                
    return max_time
        
        
            