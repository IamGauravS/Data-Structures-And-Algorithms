from collections import deque
def find_order(n, prerequisites):
    
    # Replace this placeholder return statement with your code
    graph = {}
    for pre in prerequisites:
        parent = pre[1]
        child = pre[0]
        
        if parent not in graph:
            graph[parent] = []
            
        if child not in graph[parent]:
            graph[parent].append(child)
            
    indegree = {}
    for i in range(n):
        indegree[i] = 0
        
    for node in graph:
        for child in graph[node]:
            indegree[child] +=1 
           
    q =  deque()
    for node in indegree:
        if indegree[node] == 0:
            q.append(node)
            
    topo = []
    while q:
        curr = q.popleft()
        topo.append(curr)
        if curr in graph:
            for child in graph[curr]:
                indegree[child] -=1
                if indegree[child] == 0:
                    q.append(child)
          
    if len(topo) < 2:
        return []          
    return topo
        