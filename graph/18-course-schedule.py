
import queue
def course_schedule(courses):
    
    adj_matrix = {}
    for course in courses:
        pre = course[1]
        cr = course[0]
        
        if pre not in adj_matrix:
            adj_matrix[pre] = []
            
        adj_matrix[pre].append(cr)
        
    indegree = {}
    
    for key in adj_matrix.keys():
        if key not in indegree:
            indegree[key] = 0
            
        for children in adj_matrix[key]:
            if children not in adj_matrix:
                indegree[children] = 0
            indegree[children] +=1 
            
    q = queue.Queue()
    
    for key in indegree.keys():
        if indegree[key] == 0:
            q.put(key)
   
    topo = []        
    while not q.empty():
        curr = q.get()
        topo.append(curr)
        
        for children in adj_matrix[curr]:
            indegree[children] -= 1
            if indegree[children] == 0:
                q.put(children)
                
                
    return  len(topo) == len(indegree)
        
    
            
            
        
        
    