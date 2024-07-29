
import queue
def bfs_traversal(edges, src, dest):
    
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
        
    q = queue.Queue()
    q.put((src, None))
    visited[src] = True

    output = []
    while not q.empty():
        curr= q.get()
        node = curr[0]
        parent = curr[1]
        output.append(node)
        for children in adj_matrix[node]:
            if children != parent and visited[children] == False:
                visited[children] = True 
                q.put((children, node))    
                
    return False