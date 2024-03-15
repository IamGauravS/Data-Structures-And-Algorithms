
import queue

def bfs(adj_matrix, visited, key, color):
    q = queue.Queue()
    q.put(key, 'g', -1)
    color[key] = 'g'
    visited[key] == True
    
    while not q.empty():
        curr, c, parent = q.get()
        
        for children in adj_matrix[curr]:
            if children != parent:
                if visited[children] == True:
                    if color[children] == c:
                        return False
                else:
                    if c == 'g':
                        curr_color = 'y'
                    else:
                        curr_color = 'g'
                    q.put((children, curr_color, curr))
                    
    return True 
                    
                 
            


def bipartite_graph(edges):
    
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
        
    color = {}
    for key in adj_matrix:
        color[key] = ''
        
    
    
    for key in visited.keys():
        if visited[key] == False:
            if not bfs(adj_matrix, visited, key, color):
                return False
            
    return True
        
        
    