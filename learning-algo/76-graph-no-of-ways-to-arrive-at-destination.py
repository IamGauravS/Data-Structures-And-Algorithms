
import heapq
import sys
def find_no_of_shortest_path(graph, source, dest):
    distance = {}
    for nodes in graph.keys():
        distance[nodes] = sys.maxsize

    distance[source] = 0

    heap = []
    heapq.heappush(heap, [source,0])
    no_of_ways = 0
    while heap:
        curr = heapq.heappop()
        curr_dist = curr[1]
        node = curr[0]

        for child in graph[node]:
            new_dst = curr_dist + child[1]
            if new_dst < distance[child[0]]:
                heapq.heappush(heap, [child[0], new_dst])
                distance[child[0]] = new_dst
                if child[0] == dest:
                    no_of_ways  = 1
            elif new_dst == distance[child[0]] and child[0] == dest:
                no_of_ways +=1


    print(no_of_ways)