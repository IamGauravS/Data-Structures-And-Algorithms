## [0][0] will always be the source and [n-1][n-1] will always be destination
import sys
import heapq

def get_child(maze, node):
    height = len(maze)
    width = len(maze[0])
    child = []
    delta = [(0,1), (1,0), (0, -1), (-1, 0)]
    for dx, dy in delta:
        if 0 <= node[0] +dx < height and 0 <= node[1] + dy < width:
            child.append([node[0] +dx, node[1] + dy])
    return child

def find_path_with_minimum_effort(grid):
    height = len(grid)
    width = len(grid[0])

    effort = [[sys.maxsize for i in range(height)] for j in range(width)] 
    parent = [[None for _ in range(width)] for _ in range(height)]

    effort[0][0] = 0
    heap = []
    heapq.heappush(heap, [0, [0,0]])

    while heap:
        curr_element = heapq.heappop(heap)
        curr_node = curr_element[1]
        curr_effort = curr_element[0]

        for child in get_child(grid, curr_node):

            ##The problem statement defines the "effort" of a path as the maximum absolute difference in heights between two consecutive cells of the path. It's not the sum of the absolute differences, but the maximum one.
            next_effort = max(curr_effort, abs(grid[child[0]][child[1]] - grid[curr_node[0]][curr_node[1]]))
            if next_effort < effort[child[0]][child[1]]:
                effort[child[0][child[1]]] = next_effort
                parent[child[0]][child[1]] = curr_node
                heapq.heappush(heap, [next_effort, child])

    path = []
    node = [height-1, width-1]
    while node is not None:
        path.append(node)
        node = parent[node[0]][node[1]]
    path.reverse()

    return effort[height-1][width-1]