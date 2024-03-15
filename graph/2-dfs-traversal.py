

def dfs_traversal(edges, src, dest):
    
    adj_matrix ={}
    
    ##(src <-> destination)
    for edge in edges:
        node1 = edge[0]
        node2 = edge[1]
        if node1 not in adj_matrix:
            adj_matrix[node1] = []
        if node2 not in adj_matrix:
            adj_matrix[node2] = []
            
        adj_matrix[node1].append(node2)
        adj_matrix[node2].append(node1)
        
        
    visited = {}
    for key in adj_matrix:
        visited[key] = False
        
    stack = []
    stack.append((src, None))
    
    while stack:
        curr = stack.pop()
        node = curr[0]
        parent = curr[1]
        if node == dest:
            return True 
        for children in adj_matrix[node]:
            if visited[children] == False and children != parent:
                stack.append((children, node))
                visited[children] = True 
                
    return False