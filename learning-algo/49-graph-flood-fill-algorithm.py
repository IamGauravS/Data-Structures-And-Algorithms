

def get_children(graph, source_node, graph_color):
    height = len(graph)
    width = len(graph[0])
    delta = [(1,0), (-1,0), (0,1), (0,-1)]
    children = []
    for dx, dy in delta:
        if (0 <= source_node[0] + dx < height) and (0 <= source_node[1] + dy< width):
            if graph[source_node[0] + dx][source_node[1] + dy] == graph_color:
                children.append([source_node[0] + dx, source_node[1] + dy])

    return children

def flood_fill(graph, source_node, new_color):
    height = len(graph)
    width = len(graph[0])

    visited = [[False for i in range(width)] for j in range(height)]

    stack = []
    stack.append(source_node)
    graph_color = graph[source_node[0]][source_node[1]]
    while len(stack) != 0:
        curr_node = stack.pop()
        graph[curr_node[0]][curr_node[1]] = new_color
        visited[curr_node[0]][curr_node[1]] = True 
        children = get_children(graph, curr_node, graph_color)
        for child in children:
            if visited[child[0]][child[1]] == False:
                stack.append(child)


    return graph