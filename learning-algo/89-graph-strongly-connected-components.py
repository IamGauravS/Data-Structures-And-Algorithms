from collections import defaultdict

def kosaraju(graph):
    stack = []
    visited = set()

##In Kosaraju's algorithm, the "finish time" for each vertex is implicitly tracked by the order in which vertices are added to the stack (or list) during the first depth-first search (DFS).

#In the DFS, a vertex is added to the stack only after all of its descendants have been visited. This means that a vertex is "finished" (i.e., all of its descendants have been visited) when it is added to the stack. The first vertex added to the stack is the one with the greatest finish time, and the last vertex added to the stack is the one with the smallest finish time.

#So, the stack itself serves as a record of the vertices ordered by their finish times. When we pop vertices from the stack during the second DFS on the transposed graph, we are effectively processing the vertices in order of decreasing finish time.
    
    def dfs(node):
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(neighbor)
        stack.insert(0, node)  # equivalent to appendleft in deque

    # Step 1: Order the vertices
    for node in graph:
        if node not in visited:
            dfs(node)

    # Step 2: Transpose the graph
    transposed = defaultdict(list)
    for node, neighbors in graph.items():
        for neighbor in neighbors:
            transposed[neighbor].append(node)

    # Step 3: Find strongly connected components
    visited.clear()
    scc = []
    while stack:
        node = stack.pop(0)  # equivalent to popleft in deque
        if node not in visited:
            component = []
            stack2 = [node]  # using list as stack
            while stack2:
                node = stack2.pop()
                visited.add(node)
                component.append(node)
                for neighbor in transposed[node]:
                    if neighbor not in visited:
                        stack2.append(neighbor)
            scc.append(component)

    return scc