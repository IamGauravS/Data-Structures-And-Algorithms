import heapq
import sys

def dijkstra(edges, start, dest):
    ## edges -> src, dest , weight 
    
    adj_list= {}
    distance = {}
    parent = {}
    for edge in edges:
        src, dest, wt = edge
        if src not in adj_list:
            adj_list[src] = []
        adj_list[src].append((dest, wt))
        distance[src] = sys.maxsize
        distance[dest] = sys.maxsize
        parent[src] = None 
        parent[dest] = None 
        
        
    heap = []
    heapq.heappush(heap, (0, start))
    distance[start] = 0 
    parent[start] = None 
    
    while heap:
        dist, curr = heapq.heappop(heap)
        
        for c, wt in adj_list[curr]:
            if distance[c] > wt + dist:
                distance[c] = wt + dist 
                parent[c] = curr 
                heapq.heappush(heap, (distance[c], c))
                
    output = []
    curr = dest 
    while curr != None:
        output.append(curr)
        curr = parent[curr]
        
    return output[::-1]
    
                
    
                
            