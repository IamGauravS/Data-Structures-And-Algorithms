import queue

def shortest_bridge(grid):
    def dfs(grid, i, j, visited, q):
        if visited[i][j] == True:
            return 
        visited[i][j] = True
        q.put((i, j))
        delta = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for dx, dy in delta:
            if 0 <= i + dx < len(grid) and 0 <= j + dy < len(grid[0]) and visited[i+dx][j+dy] == False and grid[i+dx][j+dy] == 1:
                dfs(grid, i + dx, j + dy, visited, q)

    height = len(grid)
    width = len(grid[0])
    visited = [[False for _ in range(width)] for _ in range(height)]
    q = queue.Queue()
    found = False

    for i in range(height):
        for j in range(width):  ## you need to break both the loops
            if grid[i][j] == 1:
                dfs(grid, i, j, visited, q)
                found = True
                break
        if found:
            break

    shortest_path = 0

    while not q.empty():
        delta = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        len_q = q.qsize()
        for _ in range(len_q):
            curr = q.get()
            i, j = curr
            for dx, dy in delta:
                if 0 <= i + dx < len(grid) and 0 <= j + dy < len(grid[0]):
                    if visited[i+dx][j+dy] == False:
                        if grid[i+dx][j+dy] == 1:
                            return shortest_path
                        else:
                            visited[i+dx][j+dy] = True
                            q.put((i+dx, j+dy))
        shortest_path += 1

    return -1