
def dfs(key, adj_matrix, visited, stack):
    if visited[key] == True:
        return
    visited[key] = True 
    for children in adj_matrix[key]:
        if visited[children] == False:
            dfs(children, adj_matrix, visited, stack)
            
    stack.append(key)
            


def topological_sort(edges):
    
    adj_matrix = {}

    ##(src -> destination)
    for edge in edges:
        node1 = edge[0]
        node2 = edge[1]
        if node1 not in adj_matrix:
            adj_matrix[node1] = []

        adj_matrix[node1].append(node2)
        
    visited = {}
    
    for key in adj_matrix:
        visited[key] = False
        
    stack = []
    for key in visited.keys():
        if visited[key] == False:
           dfs(key, adj_matrix, visited, stack)
           
    return stack[::-1]
    
    