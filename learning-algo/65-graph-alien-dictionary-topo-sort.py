## we make pairs do comparisons and continue
## create a graph and do topo sort
## here we will always start with the smallest bcoz indegree node for it will always be zero
import queue
def alien_dict_topo_sort(alien_dict):
    graph = {}

    for i in range(len(alien_dict)-1):
        s1 = alien_dict[i]
        s2 = alien_dict[i+1]
        for c1, c2 in zip(s1, s2):
            if c1 != c2:
                break 
        
        if c1 != c2:
            if c1 in graph:
                graph[c1].append(c2)
            else:
                graph[c1] = [c2]

    ## do topo sort
    indegree = {}
    for node in graph:
        indegree[node] = 0

    q = queue.Queue()

    for node in graph:
        for child in graph[node]:
            if child in indegree:
                indegree[child] +=1
            else:
                indegree[child] = 1

    for node in indegree.keys():
        if indegree[node] == 0:
            q.put(node)

    topo = []
    while not q.empty():
        curr = q.get()
        topo.append(curr)
        for child in graph[curr]:
            indegree[child] -= 1
            if indegree[child] ==0:
                q.put(child)

    return topo 
