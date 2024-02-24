## sea = 0 land = 1
import queue

def get_children(graph, i, j):
    height = len(graph)
    width = len(graph[0])
    children = []
    delta = [(0,1), (0,-1), (1,0), (-1,0)]  # Directions for the neighboring cells (up, down, left, right)

    # Loop through each direction
    for dx, dy in delta:
        # Check if the neighboring cell is within the graph boundaries
        if 0 <= i+ dx < height and 0 <= j+dy < width:
             # Check if the neighboring cell is not a wall (value is 0)
             if graph[i+ dx][j+dy] == 1:
                  # If valid, add the neighboring cell to the children list
                  children.append([i+ dx, j+dy])

    return children 

def calculate_no_of_enclaves(grid):
    height = len(grid)
    width  = len(grid[0])

    visited = [[False for j in range(width)] for i in range(height)]

    q = queue.Queue()
    for i in range(height):
        for j in range(width):
            if i==0 or j==0 or i == height-1 or j == width-1:
                if grid[i][j] == 1:
                    q.put([i,j])

    while not q.empty():
        curr = q.get()
        visited[curr[0]][curr[1]] = True 

        children = get_children(grid, curr[0], curr[1])
        for child in children:
            if visited[child[0]][child[1]] == False:
                q.put(child)


    no_of_enclaves = 0
    
    for i in range(height):
        for j in range(width):
            if visited[i][j] == False and grid[i][j] == 1:
                no_of_enclaves +=1

    return no_of_enclaves