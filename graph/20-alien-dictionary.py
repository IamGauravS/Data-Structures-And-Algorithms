
import queue
def alien_word(word_dict):
    
    edges = []
    
    for i in range(len(word_dict)-1):
        word1  = word_dict[i]
        word2 = word_dict[i+1]
        
        i = 0
        j = 0
        while i < len(word1) and j < len(word2):
            if word1[i] != word2[j]:
                 
                edges.append((word1[i], word2[j]))
                break 
            
    adj_matrix = {}
    
    for edge in edges:
        src = edge[0]
        dest = edge[1]
        
        if src not in adj_matrix:
            adj_matrix[src] = []
            
        adj_matrix[src].append(dest)
        
    indegree = {}
    
    for key in adj_matrix.keys():
        if key not in indegree:
            indegree[key] = 0
        for children in adj_matrix[key]:
            if children not in indegree:
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
        
        if curr in adj_matrix:
            for children in adj_matrix[curr]:
                indegree[children] -= 1
                if indegree[children] == 0:
                    q.put(children)
                    
    return topo   
        