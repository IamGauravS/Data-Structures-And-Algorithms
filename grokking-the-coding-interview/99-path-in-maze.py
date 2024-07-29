def number_of_paths(n, corridors):
    
    # Replace this placeholder return statement with your code
    def dfs(node, visited, path):
        if len(path) == 3:
            if path[0] in graph[node]:  ### path[0] will be starting node we are checking if it is in the end node
                return 1
            else:
                return 0
            
        visited.add(node)
        count = 0
        for neighbor in graph[node]:
            if neighbor not in visited:
                count += dfs(neighbor, visited.copy(), path + [neighbor])  ## we do visited.copy bcoz we want to check only in that path
                
        return count 
    
    
    graph = {i: set() for i in range(1, n+1)}
    for corridor in corridors:
        graph[corridor[0]].add(corridor[1])
        graph[corridor[1]].add(corridor[0])
        
    confusion_score = 0
    for node in graph:
        confusion_score += dfs(node, set(), [node])
        
    return confusion_score //6
    
            