

def dfs(matrix, visited, i, j):
    delta = [(0,1), (0,-1), (1,0), (-1,0), (1,1), (-1,1), (1,-1), (-1,-1)]
    
    visited[i][j] = True
    
    for dx, dy in delta:
        if 0 <= i+dx < len(matrix) and 0 <= j+dy < len(matrix[0]) and matrix[i+dx][j+dy] == 1 and visited[i+dx][j+dy] == False:
            dfs(matrix, visited, i+dx, j+dy)
            
    return
            


def find_no_of_islands(matrix):
    visited = [[False for i in range(len(matrix[0]))] for j in range(len(matrix))]
    
    no_of_island = 0
    
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 1 and visited[i][j] == False:
                no_of_island +=1
                dfs(matrix, visited, i, j)
                
                
    return no_of_island