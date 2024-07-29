### dijkstra algorithm
import sys 
import heapq

def network_delay_time(times, n, k):

    # Replace this placeholder return statement with your code
    graph = {}
    for time in times:
        source_node = time[0]
        dest_node = time[1]
        d = time[2]
        if source_node not in graph:
            graph[source_node]= []
        graph[source_node]. append([dest_node, d])
    
    
    
    distance = {}
    for i in range(1, n+1):
        distance[i] = sys.maxsize 
        
    distance[k] = 0
    heap = []
    heapq.heappush(heap, [0, k])
    
    while heap:
        curr_elem= heapq.heappop(heap)
        curr_distance = curr_elem[0]
        curr_node = curr_elem[1]
        
        if curr_node in graph:
            for child in graph[curr_node]:
                if distance[child[0]] > curr_distance + child[1]:
                    distance[child[0]] = curr_distance + child[1]
                    heapq.heappush(heap, [distance[child[0]], child[0]])
                
    max_dist = max(distance.values())
    return max_dist if max_dist < sys.maxsize else -1
    
    
    
    
        
    