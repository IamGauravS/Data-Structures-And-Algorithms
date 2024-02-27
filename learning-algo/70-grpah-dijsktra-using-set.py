import sys 
## use priority queue
def dijsktra_algorithm(graph, source_node):
    distance = {}
    for node in graph:
        distance[node] = sys.maxsize

    distance[source_node] = 0
    visited = set()

    while True:
        min_distance_node = None
        for node in distance:
            if node not in visited:
                if min_distance_node is None:
                    min_distance_node = node
                elif distance[node] < distance[min_distance_node]:
                    min_distance_node = node

        if min_distance_node is None:
            break

        visited.add(min_distance_node)
        current_distance = distance[min_distance_node]

        for edge in graph[min_distance_node]:
            distance[edge[0]] = min(current_distance + edge[1], distance[edge[0]])

    return distance