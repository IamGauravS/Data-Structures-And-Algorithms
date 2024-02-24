def get_children(graph, visited, curr_node):
    height = len(graph)
    width = len(graph[0])
    children = []
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
    for dx, dy in directions:
        new_x, new_y = curr_node[0] + dx, curr_node[1] + dy
        if 0 <= new_x < height and 0 <= new_y < width and graph[new_x][new_y] == 1 and visited[new_x][new_y] == -1:
            children.append([new_x, new_y])
    return children

def dfs(graph, visited, i, j):
    stack = []
    stack.append([i, j])
    while stack:
        curr_node = stack.pop()
        visited[curr_node[0]][curr_node[1]] = 1
        children = get_children(graph, visited, curr_node)
        for child in children:
            stack.append(child)

def find_num_of_island(grid):
    height = len(grid)
    width = len(grid[0])
    visited = [[-1 for _ in range(width)] for _ in range(height)]
    for i in range(height):
        for j in range(width):
            if grid[i][j] == 0:
                visited[i][j] = 0   # 0 for water  

    count_island = 0
    for i in range(height):
        for j in range(width):
            if visited[i][j] == -1:  # -1 for unvisited land
                count_island += 1
                dfs(grid, visited, i, j)

    return count_island