## we use bellman ford algorithm when graph has negative edges , negative cycle, can only be used for directed graph
## to use for undirected graph just convert undirected to directed 

import sys

def bellmanford_algorithm(edges, source, destination):
    
    ## edges can be given in any particular order 
    ## src, dest, wt
    
    ## relax all the edges n-1 times sequentially 
    distance = {}
    for edge in edges:
        src, dest, wt = edge 
        if src not in distance:
            distance[src] = sys.maxsize 
        if dest not in distance:
            distance[dest] = sys.maxsize 
            
    no_of_nodes = len(distance)
    distance[source] = 0
    
    for _ in range(no_of_nodes-1):
        for edge in edges:
            src, dest, wt = edge
            if distance[dest] > distance[src] + wt:
                distance[dest] = distance[src] + wt 
                
    # Check for negative weight cycles
    for edge in edges:
        src, dest, wt = edge
        if distance[dest] > distance[src] + wt:
            raise ValueError("Graph contains a negative-weight cycle")
                
                
    return distance[dest]
    
    