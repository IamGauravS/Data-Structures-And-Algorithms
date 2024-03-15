

def dfs(src, visited, adj_matrix):
    if visited[src] == True:
        return 
    visited[src] = True 
    
    for children in adj_matrix[src]:
        if children != src and visited[children] == False:
            dfs(children, visited, adj_matrix)
    return 


def find_no_of_provinces(edges):
    
    adj_matrix = {}
    
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
        
    count = 0 
    
    for key in visited:
        if visited[key] == False:
            count +=1
            dfs(key, visited, adj_matrix)
            
    return count 