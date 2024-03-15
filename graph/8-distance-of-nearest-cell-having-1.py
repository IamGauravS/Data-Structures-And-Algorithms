

import queue
import sys
def distance_of_nearest_cell(matrix):
    output_matrix = [[sys.maxsize for i in range(len(matrix[0]))] for j in range(len(matrix))]
    
    
    q = queue.Queue()
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 1:
                q.put((i,j, 0))
                output_matrix[i][j] = 0
    
    
    delta = [(1,0), (0,1), (-1,0), (0,-1)]
    while not q.empty():
        i,j,time = q.get()
        
        for dx, dy in delta:
            if 0 <= i+dx < len(matrix) and 0 <= j+dy < len(matrix[0]) and matrix[i+dx][j+dy] == 0:
                curri = i+dx
                currj = j+dy 
                
                if output_matrix[curri][currj] > time+1:
                    output_matrix[curri][currj] = time+1
                    q.put((curri, currj, time+1))
                    
                    
    return output_matrix        