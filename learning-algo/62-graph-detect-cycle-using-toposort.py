import queue

def detect_cycle_using_toposort(graph):
    indegree = [0 for i in range(len(graph))]

    for node in graph:
        for child in graph[node]:
            indegree[child] +=1 

    q = queue.Queue()
    for node in graph:
        if indegree[node] == 0:
            q.put(node)

    topo = []
    while not q.empty():
        curr = q.get()
        topo.append(curr)
        for child in graph[curr]:
            indegree[child] -=1
            if indegree[child] == 0:
                q.put(child)

    if len(topo) != len(graph):
        return True 
    return False