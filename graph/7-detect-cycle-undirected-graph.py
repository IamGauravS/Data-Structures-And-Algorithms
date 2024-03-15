
import queue

def bfs(visited, adj_matrix, key):
    q = queue.Queue()
    q.put((key, -1))
    visited[key] = True 
    
    while not q.empty():
        curr, parent = q.get()
        
        for children in adj_matrix[curr]:
            if visited[children] == True and children != parent:
                return False
            else:
                if visited[children] == False and children != curr:
                    q.put((children, curr))
                    
    return True



def detect_cycle(edges):
    
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
        
    for key in visited.keys():
        if visited[key] == False:
            flag = bfs(visited, adj_matrix, key)
            
            if not flag:
                return True 
            
            
    return False 