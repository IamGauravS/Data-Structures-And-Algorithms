### 0 empty cell, 1 fresh  2 rotten
import queue


def get_children(graph, i,j):
    height = len(graph)
    width = len(graph[0])
    delta = [(0,1), (0,-1), (1, 0), (-1, 0)]
    children = []

    for dx, dy in delta:
        if (0 <= i+dx < height) and (0 <= j+dy < width):
            if graph[i+dx][j+dy] == 1:
                children.append([i+dx, j+dy])

    return children

def time_for_rotten_oranges(graph):
    height = len(graph)
    width = len(graph[0])

    visited = [[0 for i in range(width)] for j in range(height)]

    q = queue.Queue()
    for i in range(height):
        for j in range(width):
            if graph[i][j] == 2:
                q.put([i,j,0])

    max_time = 0
    while not q.empty():
        curr_node = q.get()
        curr_time = curr_node[2]
        if max_time < curr_time:
            max_time = curr_time

        visited[curr_node[0]][curr_node[1]] = True 
        children = get_children(graph, curr_node[0], curr_node[1])
        for child in children:
            if visited[child[0]][child[1]] == False:
                q.put([child[0], child[1], curr_time+1])

    return max_time