
import queue 
def find_evantual_safe_states(edges):
    ## edge is source - > destination but we will store them in opposite direction and do topo on that 
    
    adj_matrix = {}
    for course in edges:
        pre = course[1]
        cr = course[0]
        
        if cr not in adj_matrix:
            adj_matrix[cr] = []
            
        adj_matrix[cr].append(pre)
        
    indegree = {}
    
    for key in adj_matrix.keys():
        if key not in indegree:
            indegree[key] = 0
            
        for children in adj_matrix[key]:
            if children not in adj_matrix:
                indegree[children] = 0
            indegree[children] +=1 
            
    topo = []
    
    q = queue.Queue()
    for key in indegree.keys():
        if indegree[key] == 0:
            q.put(key)
            
    while not q.empty():
        curr = q.get()
        topo.append(curr)
        
        for children in adj_matrix[curr]:
            indegree[children] -=1 
            if indegree[children] == 0:
                q.put(children)
                
    return topo
            
            
            