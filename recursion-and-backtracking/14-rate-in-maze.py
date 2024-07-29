


def find_all_paths_helper(maze, i, j, path, output, visited):
    if i == len(maze)-1 and j == len(maze[0])-1:
        output.append(path)
        return 
        
    if visited[i][j] == True:
        return
    
    visited[i][j] = True
        
    delta = [(0,1), (1,0), (0,-1), (-1,0)]
    
    for dx, dy in delta:
        newi = i+dx
        newj = j+dy 
        if 0 <= newi < len(maze) and 0 <= newj < len(maze[0]) and visited[newi][newj] == False and maze[newi][newj] != 0:
             path.append((newi, newj))
             find_all_paths_helper(maze, newi, newj, path, output, visited)
             path.pop()
             
    visited[i][j] = False 
    
    return 
             
             
def find_all_path(maze):
    output= []
    path = []
    visited = [[False for i in range(len(maze[0]))] for j in range(len(maze))]
    
    find_all_paths_helper(maze, 0,0, path, output, visited)
    
    return output