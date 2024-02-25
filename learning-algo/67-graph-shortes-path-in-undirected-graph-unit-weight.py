import sys 
import queue

def find_distance_undirected_graph_weight(graph, source):
    """
    This function implements a Breadth-First Search (BFS) algorithm to find the shortest path 
    (in terms of number of edges) from the source to all other nodes in an unweighted, undirected graph.

    In BFS, we explore the nodes level by level, starting from the source. When we visit a node, 
    we consider all its unvisited neighbors and update their distances. If the distance to a neighbor 
    is updated, it means we've found a shorter path to that neighbor through the current node. 
    So, we add that neighbor to the queue to explore its own neighbors in subsequent iterations.

    If the distance to a neighbor is not updated, it means we've already found a shorter or equal 
    path to that neighbor before. So, we don't need to add it to the queue again. Adding it to the 
    queue again would just result in unnecessary computations, as we would be considering its neighbors 
    again even though we know we can't find a shorter path to them through this node.

    This approach ensures that each node is enqueued and dequeued at most once, giving the algorithm 
    a time complexity of O(V + E), where V is the number of vertices and E is the number of edges.
    """

    distance = {}
    for node in graph:
        distance[node] = sys.maxsize

    distance[source] = 0  # source node has zero distance 

    q = queue.Queue()
    q.put(source)  

    while not q.empty():
        curr = q.get()
        for child in graph[curr]:
            if distance[curr] + 1 < distance[child]:  # check and update the distance of the child
                distance[child] = distance[curr] + 1
                q.put(child)  # add the child to the queue

    return distance