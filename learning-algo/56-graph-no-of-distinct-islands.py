# This function returns all neighboring land cells of a given cell.
def find_children(grid, visited, curr):
    height= len(grid)
    width = len(grid[0])
    children = []
    delta = [(0,1), (0,-1), (-1,0), (1,0)]
    for dx, dy in delta:
        if 0 <= curr[0] + dx < height and 0 <= curr[1] + dy < width and grid[curr[0] + dx][curr[1] + dy] == 1:
            children.append([curr[0] + dx, curr[1] + dy])

    return children

# This function performs a depth-first search (DFS) starting from a given cell, 
# visiting all reachable land cells and returning their relative positions to the starting cell. 
# This way, each island is represented by a tuple of relative positions, 
# which allows us to compare islands by their shape and orientation.
def find_island(grid, visited, i, j):
    stack = []
    stack.append([i,j])
    output_list = []
    while len(stack) != 0:
        curr = stack.pop()
        visited[curr[0]][curr[1]] = True 
        output_list.append([curr[0]-i, curr[1]-j])
        children = find_children(grid, visited, curr)
        for child in children:
            if visited[child[0]][child[1]] == False:
                stack.append([child[0], child[1]])

    return tuple(output_list)

# This function loops through all cells in the grid. 
# If a land cell is found that has not been visited, 
# it calls find_island to get the representation of the island that this cell belongs to. 
# It then adds this representation to a set of unique islands.
# Finally, the function returns the number of unique islands in the set.
def no_of_island(grid):
    height= len(grid)
    width = len(grid[0])

    visited = [[False for j in range(width)] for i in range(height)]

    unique_island_set = set()

    for i in range(height):
        for j in range(width):
            if grid[i][j] == 1 and visited[i][j] == False:
                curr_island = find_island(grid, visited, i,j)
                if curr_island not in unique_island_set:
                    unique_island_set.add(curr_island)

    return len(unique_island_set)