

def dfs(matrix, visited, i, j , islands, src):
    if visited[i][j] == True:
        return
    visited[i][j] = True 
    islands.append((i-src[0], j-src[1]))
    delta = [(0,1), (1,0), (-1,0), (0,-1)]
    
    for dx, dy in delta:
        if 0 <= i+dx < len(matrix) and 0 <= j+dy < len(matrix[0]) and matrix[i+dx][j+dy] == 1 and visited[i+dx][j+dy] == False:
            dfs(matrix, visited, i+dx, j+dy, islands, src)
            
    return


def no_of_distinct_island(matrix):
    island_set = set()
    
    visited = [[False for i in range(len(matrix[0]))] for j in range(len(matrix))]
    
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 1 and visited[i][j] == False:
                islands = []
                dfs(matrix, visited, i, j, islands, (i,j))
                
                island_set.add(islands)
            
            
    return len(island_set)