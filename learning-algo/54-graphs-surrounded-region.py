
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
             if graph[i+ dx][j+dy] == 0:
                  # If valid, add the neighboring cell to the children list
                  children.append([i+ dx, j+dy])

    return children 

## This code now correctly finds the area surrounded by 1s in the grid and fills it with 1s. It performs a breadth-first search on the grid starting from all cells with value 0 on the border, and marks all reachable cells with value 0 as visited. Then it loops through all cells in the grid and changes the value of all unvisited cells with value 0 to 1.
def find_area_surronded_by_region(grid):
    height = len(grid)
    width = len(grid[0])

    visited = [[False for i in range(width)] for j in range(height)]
    q = queue.Queue()

    ## add corner 0s to queue
    for i in range(height):
        for j in range(width):
            if i == 0 or j==0 or i == height-1 or j == width-1:
                if grid[i][j] == 0:
                    q.put([i,j])

    while not q.empty():
        curr_node = q.get()
        visited[curr_node[0]][curr_node[1]] = True 
        children = get_children(grid, curr_node[0], curr_node[1])
        for child in children:
            if visited[child[0]][child[1]] == False:
                q.put([child[0], child[1]])

    
    for i in range(height):
        for j in range(width):
            if grid[i][j] == 0 and visited[i][j] == False:
                grid[i][j] =1 

    return grid 