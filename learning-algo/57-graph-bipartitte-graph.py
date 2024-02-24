def dfs(graph, node, color):
    # Color the node
    colored[node] = color

    # For each child of the current node
    for child in graph[node]:
        # If the child has not been colored yet
        if colored[child] is None:
            # Recursively call dfs for the child with the opposite color
            if not dfs(child, 'y' if color == 'r' else 'r'):
                return False
        # If the child has been colored and its color is the same as the current node
        elif colored[child] == color:
            # Return False as the graph is not bipartite
            return False

    # If all children have been processed and no conflicts have been found, return True
    return True

def bipartite_graph(graph):
    global colored
    colored = [None] * len(graph)

    # For each node in the graph
    for node in range(len(graph)):
        # If the node has not been colored yet
        if colored[node] is None:
            # Call dfs for the node with color 'y'
            if not dfs(graph, node, 'y'):
                return False

    # If all nodes have been processed and no conflicts have been found, return True
    return True