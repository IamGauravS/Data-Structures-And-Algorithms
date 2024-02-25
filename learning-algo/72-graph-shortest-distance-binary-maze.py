import queue
import sys
def get_child(maze, node):
    height = len(maze)
    width = len(maze[0])
    child = []
    delta = [(0,1), (1,0), (0, -1), (-1, 0)]
    for dx, dy in delta:
        if 0 <= node[0] +dx < height and 0 <= node[1] + dy < width:
            if maze[node[0] +dx][node[1] + dy] == 1:
                child.append([node[0] +dx, node[1] + dy])
    return child

def calculate_shortest_distance(maze, source, target):
    height = len(maze)
    width = len(maze[0])

    q = queue.Queue()
    q.put([source, 0])

    dist = [[sys.maxsize for i in range(width)] for j in range(height)]
    dist[source[0]][source[1]] = 0

    while q:
        curr = q.get()
        node = curr[0]
        curr_dist = curr[1]
        children = get_child(maze, node)
        for child in children:
            if dist[child[0]][child[1]] >= curr_dist + 1:
                dist[child[0]][child[1]] = curr_dist + 1
                q.put([child, dist[child[0]][child[1]]])

            if child == target:
                return dist[child[0]][child[1]]