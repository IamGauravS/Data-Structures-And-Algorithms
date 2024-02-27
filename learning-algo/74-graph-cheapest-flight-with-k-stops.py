import queue
import sys

def find_cheapest_flight_with_k_stops(graph, source, target, k):
    distance = {}
    for node in graph:
        distance[node] = sys.maxsize

    distance[source] = 0
    q = queue.Queue()
    ## [no of stops, distance, node]
    q.put([0, 0, source])

    while not q.empty():
        curr = q.get()
        dst = curr[1]
        stops = curr[0]
        node = curr[2]
        
        for child in graph[node]:
            new_dst = child[1] + dst 
            temp_stop = stops + 1
            if new_dst < distance[child[0]] and temp_stop <= k:
                distance[child[0]] = new_dst
                q.put([temp_stop, new_dst, child[0]])

    return distance[target] if distance[target] != sys.maxsize else -1