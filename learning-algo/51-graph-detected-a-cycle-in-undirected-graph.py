### we use bfs traversal to find cycle in undirected graph
import queue

def find_cycle_undirected_graph(graph, source_node):
    visited = [False]*len(graph)
    parent = [-1]*len(graph)

    q = queue.Queue()
    q.put(source_node)

    while not q.empty():
        curr_node = q.get()
        if visited[curr_node] == True:
            return False 
        children = graph[curr_node]
        visited[curr_node] = True 
        for child in children:
            if visited[child] == False:
                q.put(child)
                parent[child] = curr_node
            elif parent[curr_node] != child:
                return True 

    return True

