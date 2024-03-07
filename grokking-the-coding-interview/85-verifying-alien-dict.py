from collections import deque
def verify_alien_dictionary(words, order):
  
    # Replace this placeholder return statement with your code
    graph = {}
    
    for  i in range(1, len(words)):
        word1 = words[i-1]
        word2 = words[i]
        
        for c1, c2 in zip(word1, word2):
            if c1 != c2:            
                if c1 not in graph:
                    graph[c1] = []
                if c2 not in graph[c1]:
                    graph[c1].append(c2)
                break
                        
    indegree = {}
    for node in graph:
        indegree[node] = 0
    
    for node in graph:
        for child in graph[node]:
            if child in indegree:
                indegree[child] +=1
            else:
                indegree[child] = 1
                
    q = deque()
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
                        
    i = 0
    j = 0
    while i < len(topo) and j < len(order):
        if topo[i] == order[j]:
            i+=1
            j+=1
        else:
            j+=1
                
    if i == len(topo):
            return True 
    else:
            return False 
            
                    
            