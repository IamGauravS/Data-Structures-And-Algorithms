
import queue
import sys
def find_shortest_path(edges, src):
    adj_list = {}
    
    for edge in edges:
        node1 = edge[0]
        node2 = edge[1]
        
        if node1 not in adj_list:
            adj_list[node1] = []
        if node2 not in adj_list:
            adj_list[node2] = []
            
        adj_list[node1].append(node2)
        adj_list[node2].append(node1)
        
        
    distance = {}
    for key in adj_list.keys():
        distance[key] = sys.maxsize
        
    distance[src] = 0
    q = queue.Queue()
    q.put((src, 0))
    
    while not q.empty():
        node, curr_distance = q.get()
        distance[node] = curr_distance
        
        for children in adj_list[node]:
            if distance[children] > 1 + curr_distance:
                distance[children] = curr_distance + 1
                q.put((children, distance[children]))
                
                
    return distance
    
        
    