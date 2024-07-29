

import heapq 
import sys 

def find_number_of_shortest_path(edges, start, end):
    ## start, end, wt  bidirectional
    adj_list = {}
    ways = {}
    distance = {}
    for edge in edges:
        node1, node2, wt = edge 
        if node1 not in adj_list:
            adj_list[node1]= []
        if node2 not in adj_list:
            adj_list[node2] = []
        adj_list[node1].append((node2, wt))
        adj_list[node2].append((node1, wt))
        ways[node1], ways[node2] = 0, 0
        distance[node1], distance[node2] = sys.maxsize, sys.maxsize
        
    heap = []
    ways[start] = 1
    distance[start] = 0
    
    heapq.heappush(heap, (0, start))
    
    while heap:
        curr = heapq.heappop()
        dest, curr_node = curr 
        
        for children, wt in adj_list[curr_node]:
            if distance[children] > dest + wt:
                distance[children] = dest + wt 
                ways[children] =  ways[curr_node]
                heapq.heappush(heap, (distance[children], children))
            
            elif distance[children] == dest + wt:
                ways[children] = ways[children] + ways[curr_node]
                
                
    return ways[end]
                
            
    
    
        
        