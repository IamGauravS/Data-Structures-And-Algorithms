def dfs_detect_cycle(graph, node, parent, visited):
    # If the current node is already visited, it means we've found a cycle, so return True
    if visited[node] == True:
        return True 

    # Mark the current node as visited
    visited[node] = True

    # For each child of the current node
    for child in graph[node]:
        # If the child is not visited
        if visited[child] == False:
            # Recursively call the function for the child, passing the current node as the parent
            # If the recursive call returns True, it means a cycle was found, so return True
            if dfs_detect_cycle(graph, child, node, visited):
                return True 
        # If the child is the parent, it's not a cycle, just a back-edge to the parent, so continue to the next child
        elif child == parent:
            continue
        # If the child is visited and it's not the parent, it means we've found a cycle, so return True
        else:
            return True 

    # If no cycle is found after visiting all children, return False
    return False  