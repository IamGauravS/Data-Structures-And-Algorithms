### useful for cases where we need to find shortest path 
## given a source node u have to find the distance to every node
## everytime u get a distance which is better then the current distance u put it in the priority queueu
import sys 
import heapq

def dijsktra_algorithm(graph, source_node):
    distance = {}
    for node in graph:
        distance[node[0]] = sys.maxsize

    distance[source_node] = 0
    heap = []
    heapq.heappush(heap, [0, source_node])  ## put distance first

    while heap:
        curr_element = heapq.heappop(heap)
        curr_node = curr_element[1]
        curr_dist = curr_element[0]
        for child in graph[curr_node]:
            if distance[child[0]] > curr_dist + child[1]:
                distance[child[0]] = curr_dist + child[1]
                heapq.heappush(heap, [distance[child[0]], child[0]])

    return distance
