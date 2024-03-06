from collections import deque

def can_finish(num_courses, prerequisites):

    # Replace this placeholder return statement with your code
    indegree = {}
    for i in range(num_courses):
        indegree[i] = 0
        
    for i, prereq in enumerate(prerequisites):
        for course in prereq:
            indegree[course] +=1
            
    q = deque()
    for node in indegree:
        if indegree[node] == 0:
            q.append(node)
            
    topo = []
    while q:
        curr= q.popleft()
        topo.append(curr)
        
        for child in prerequisites[curr]:
            indegree[child] -=1
            if indegree[child] == 0:
                topo.append(child)
                
    if len(topo) == num_courses:
        return True 
    else:
        return False
        
        
