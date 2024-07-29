def valid_tree(n, edges):

    # Replace this placeholder return statement with your code
    visited = [False]*n 
    
    graph = {}
    for edge in edges:
        a = edge[0]
        b = edge[1]
        if a not in graph:
            graph[a] = set()
        if b not in graph:
            graph[b] = set()
            
        graph[a].add(b)
        graph[b].add(a)
        
    stack = []
    stack.append((edges[0][0], None))
    
    while stack:
        elem = stack.pop()
        node, parent = elem
        if visited[node] == True:  ### cycle is there
            return False
        
        visited[node] = True 
        
        for child in graph[node]:
            if child != parent:
                stack.append((child, node))
            
    
    if not all(visited):
        return False 
    
    return True