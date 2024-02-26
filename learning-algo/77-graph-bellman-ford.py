##input format [list of edges] [u, v, wt]
## edges can be given in any order
## relax all the edges n-1 times sequentially
## relax -> if dist[u] + wt < dist[v] dist[v] = dist[u] + w  (this is called relaxation of edges and will be done n-1 times n is number of vertices)
## source as zero and everything is infinity
import sys

def bellman_ford_algorithm(edges, source):
    dist = {}
    for edge in edges:
        if edge[0] not in dist:
            dist[edge[0]] = sys.maxsize 
        if edge[1] not in dist:
            dist[edge[1]] = sys.maxsize

    dist[source] = 0

    for _ in range(len(dist) - 1):  # Repeat |V| - 1 times
        for edge in edges:
            u = edge[0]
            v = edge[1]
            wt = edge[2]

            if dist[u] != sys.maxsize and dist[u] + wt < dist[v]:
                dist[v] = dist[u] + wt

    return dist


