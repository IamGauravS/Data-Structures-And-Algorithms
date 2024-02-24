# Function to perform a depth-first search (DFS) from a given node
def dfs(graph, node, visited, stack):
    # Mark the node as visited
    visited[node] = True

    # Visit all unvisited children of the node
    for child in graph[node]:
        if visited[child] == False:
            dfs(graph, child, visited, stack)

    # Add the node to the stack after all its children have been visited
    stack.append(node)
    return

# Function to perform a topological sort on the graph using DFS
def topological_sort_using_dfs(graph):
    # Initialize a list of visited nodes
    visited = [False for i in range(len(graph))]

    # Initialize a stack to hold nodes in topological order
    stack = []

    # Perform a DFS from each unvisited node in the graph
    for node in graph:
        if visited[node] == False:
            dfs(graph, node, visited, stack)

    # Initialize a list to hold the output
    output_list = []

    # Pop nodes from the stack and add them to the output list
    # Nodes are popped from the stack in last-in-first-out order, so the output list ends up being in topological order
    while stack:
        output_list.append(stack.pop())

    # Return the output list
    return output_list