

def number_of_enclaves(matrix):
    
    visited = [[False for i in range(len(matrix[0]))] for j in range(len(matrix))]
    
    
    stack = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if (i == 0 or j == 0 or i == len(matrix)-1 or j == len(matrix[0])-1) and matrix[i][j] == 1:
                visited[i][j] = True 
                stack.append([i,j])
                
     
    delta = [(0,1), (1,0), (0,-1), (-1,0)]           
    while stack:
        i, j = stack.pop()
        
        for dx, dy in delta:
            if 0 <= i+dx < len(matrix) and 0 <= j+dy < len(matrix[0]) and matrix[i+dx][j+dy] == 1 and visited[i+dx][j+dy] == False:
                visited[i+dx][j+dy] = True 
                stack.append([i+dx, j+dy])
                
                
    count = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 1 and visited[i][j] == False:
                count +=1
                
                
    return count
        
                
    
    