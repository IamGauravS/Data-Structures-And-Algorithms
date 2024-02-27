## try to remember where I am coming from and then backtrack
import heapq
import sys
def print_shortest_path(graph, source, dest):
    distance = {}
    parent = {}
    for node in graph:
        distance[node[0]] = sys.maxsize
        parent[node[0]] = None

    heap = []
    heapq.heappush(heap, [0, source])

    

    while heap:
        curr_elem = heapq.heappop(heap)
        dst = curr_elem[0]
        curr_node = curr_elem[1]
        for child in graph[curr_node]:
            if distance[child[0]] > dst + child[1]:
                distance[child[0]] = dst + child[1]
                parent[child[0]] = curr_node
                heapq.heappush(heap, [distance[child[0]], child[0]])


    output_list = []
    curr_node = dest 
    while curr_node != source:
        output_list.append(curr_node)
        curr_node = parent[curr_node]
    output_list.append(source)
    output_list.reverse()
    return output_list
