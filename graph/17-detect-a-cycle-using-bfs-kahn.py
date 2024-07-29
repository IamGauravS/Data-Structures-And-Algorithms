
## the idea is that is there is a cycle then there will be atleast one node whose indegree will never be zero
## so we just compare the number on nodes in output with total no of node and if it is less then there is a cycle


import queue
def kahns_algorithm(edges):
    
    adj_matrix = {}

    ##(src -> destination)
    for edge in edges:
        node1 = edge[0]
        node2 = edge[1]
        if node1 not in adj_matrix:
            adj_matrix[node1] = []

        adj_matrix[node1].append(node2)



    indegree = {}
    
    for key in adj_matrix:
        for children in adj_matrix[key]:
            if children not in indegree:
                indegree[children] = 0
            if key not in indegree:
                indegree[key] = 0
            indegree[children] +=1 
            
    q = queue.Queue()
    
    for key in indegree:
        if indegree[key] == 0:
            q.put(key)
            
    output = []
    
    while not q.empty():
        curr = q.get()
        output.append(curr)
        for children in adj_matrix[curr]:
            indegree[children] -=1
            if indegree[children] == 0:
                q.put(children)
                
    
    return len(output) == len(indegree.keys())
        