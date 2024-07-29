def iscycle(adj_matrix, visited, stack, key):
    visited[key] = True
    stack[key] = True

    if key in adj_matrix:
        for children in adj_matrix[key]:
            if not visited[children]:
                if iscycle(adj_matrix, visited, stack, children):
                    return True
            elif stack[children]:  # If the node is in the recursion stack, then it's a cycle
                return True

    stack[key] = False  # Remove the node from the recursion stack
    return False

def detect_cycle_directed_graph(edges):
    adj_matrix = {}

    ##(src -> destination)
    for edge in edges:
        node1 = edge[0]
        node2 = edge[1]
        if node1 not in adj_matrix:
            adj_matrix[node1] = []

        adj_matrix[node1].append(node2)

    visited = {}
    stack = {}
    for key in adj_matrix:
        visited[key] = False
        stack[key] = False

    for key in visited.keys():
        if not visited[key]:
            if iscycle(adj_matrix, visited, stack, key):
                return True 

    return False