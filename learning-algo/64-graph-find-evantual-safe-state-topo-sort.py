## all the terminal nodes are safe node
## reverse all the exsisting edges
## get all the nodes with indegree zero
## put the terminal nodes(indegree zero) in queue
## do topo sort
## all safe nodes are the one in topo list
## This solution works because in the reversed graph, a node is safe if and only if all its children are safe. So, by performing a topological sort on the reversed graph, we ensure that a node is only considered safe after all its children have been determined to be safe.

import queue

def find_evantual_safe_state_using_topo_sort(graph):
    graph_reversed = {}

    for node in graph.keys():
        for child in graph[node]:
            if child in graph_reversed:
                graph_reversed[child].append(node)
            else:
                graph_reversed[child] = [node]

    indegree = {}
    for node in graph:
         indegree[node] = 0

    for node in graph_reversed:
        for child in graph_reversed[node]:
                indegree[child] +=1

    q = queue.Queue()
    for node in indegree.keys():
            if indegree[node] ==0:
                 q.put(node)

    topo = []
    while not q.empty():
         curr = q.get()
         topo.append(curr)
         for child in graph_reversed[curr]:
              indegree[child] -= 1
              if indegree[child] ==0:
                   q.put(child)

    ## all the nodes in topo are the nodes for graph in safe state
    return topo
