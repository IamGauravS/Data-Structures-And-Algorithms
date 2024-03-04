import math
import sys

def update_matrix_helper(mat, distance_matrix, visited, i, j):
    if visited[i][j] == True:
        return distance_matrix[i][j]
    
    visited[i][j] = True
    if mat[i][j] == 0:
        distance_matrix[i][j] = 0 
        return distance_matrix[i][j]
    
    else:
        delta = [(0,1), (1,0), (-1, 0), (0,-1)]
        min_value = sys.maxsize
        for dx, dy in delta:
            if 0 <= dx + i < len(mat) and 0 <= dy + j < len(mat[0]):
                temp_dist = 1 + update_matrix_helper(mat, distance_matrix, visited, i+dx, j+dy)
                if temp_dist < min_value:
                    min_value = temp_dist
                    
        distance_matrix[i][j] = min_value
        return distance_matrix[i][j]
    

def update_matrix(mat):

    # Replace this placeholder return statement with your code
    visited = [[False for i in range(len(mat[0]))] for j in range(len(mat))]
    distance_matrix = [[sys.maxsize for i in range(len(mat[0]))] for j in range(len(mat))]
    
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if visited[i][j] == False:
                update_matrix_helper(mat, distance_matrix, visited, i, j)
                
    return distance_matrix

## the above approach also takes o(n) of time since it visits each cell only once but it can lead to a huge stack size
## bfs is a better approach here since the stack size will be smaller

from collections import deque

def update_matrix(mat):
    m, n = len(mat), len(mat[0])
    dist = [[float('inf')]*n for _ in range(m)]
    queue = deque()

    for i in range(m):
        for j in range(n):
            if mat[i][j] == 0:
                dist[i][j] = 0
                queue.append((i, j))

    dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    while queue:
        x, y = queue.popleft()
        for dx, dy in dirs:
            nx, ny = x + dx, y + dy
            if 0 <= nx < m and 0 <= ny < n and dist[nx][ny] > dist[x][y] + 1:  ## here we only update if the current distance is bigger
                dist[nx][ny] = dist[x][y] + 1
                queue.append((nx, ny))

    return dist