
def iscycle(adj_matrix, visited, stack, key, path):
    visited[key] = True
    stack[key] = True
    path.append(key)
    if key in adj_matrix:
        for children in adj_matrix[key]:
            if not visited[children]:
                if iscycle(adj_matrix, visited, stack, children):
                    return True
            elif stack[children]:  # If the node is in the recursion stack, then it's a cycle
                return True

    stack[key] = False  # Remove the node from the recursion stack
    return False

def find_eventual_safe_state(edges):
    ## every path ends up on a terminal node
    
    ## any node that is the part of cycle is not a safe node 
    
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
        
    output = []
    for key in visited.keys():
        if not visited[key]:
            path = []
            if not iscycle(adj_matrix, visited, stack, key, path):
                output += path
                
                
    return output