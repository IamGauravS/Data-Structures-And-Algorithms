import queue

# Function to get the valid children of a cell in the graph
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
### here we start with 1s firs and then there zero children and continue 
# Function to calculate the nearest cell for each cell in the graph
def calculate_nearest_cell(graph):
    height = len(graph)
    width = len(graph[0])

    # Initialize the distance matrix with 0s
    distance = [[0 for _ in range(width)] for _ in range(height)]
    # Initialize the visited matrix with False
    visited = [[False for _ in range(width)] for _ in range(height)]

    q = queue.Queue()
    # Enqueue all cells with value 0
    for i in range(height):
        for j in range(width):
            if graph[i][j] == 0:
                q.put([i,j,0])

    # Perform BFS on the graph
    while not q.empty():
        curr_node = q.get()
        # Update the distance of the current cell
        distance[curr_node[0]][curr_node[1]] = curr_node[2]
        # Mark the current cell as visited
        visited[curr_node[0]][curr_node[1]] = True

        # Get the valid children of the current cell
        children = get_children(graph, curr_node[0], curr_node[1])
        # Loop through each child
        for child in children:
            # If the child has not been visited yet, enqueue it with a distance one greater than the current cell
            if visited[child[0]][child[1]] == False:
                q.put([child[0], child[1], curr_node[2]+1])

    # Return the distance matrix
    return distance