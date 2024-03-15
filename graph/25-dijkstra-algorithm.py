

import heapq
import sys

def dijkstra(edges, start):
    ## edges -> src, dest , weight 
    
    adj_list = {}
    distance = {}
    
    
    for edge in edges:
        src, dest, weight = edge 
        
        if src not in adj_list:
            adj_list[src] = []
            
        adj_list[src].append((dest, weight))
        distance[src] = sys.maxsize 
        distance[dest] = sys.maxsize
        
    distance[start] = 0
    
    heap = []
    heapq.heappush(heap, (src, 0))
    
    while heap:
        curr, d = heapq.heappop()
        
        for children in adj_list[curr]:
            node, wt = children 
            
            if distance[node] > wt + d:
                distance[node] = wt + d 
                heapq.heappush(heap, (node, distance[node]))
            
             
            
    return distance