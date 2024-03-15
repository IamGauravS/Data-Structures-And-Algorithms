from collections import defaultdict, deque

def find_shortest_path(edges, start):
    # edge = (src, destination, weight)

    # Step 1: Topological Sort
    adj_list = defaultdict(list)
    indegree = defaultdict(int)
    for src, dest, _ in edges:
        adj_list[src].append(dest)
        indegree[dest] += 1

    q = deque([node for node in indegree if indegree[node] == 0])
    topo_order = []

    while q:
        node = q.popleft()
        topo_order.append(node)
        for neighbor in adj_list[node]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                q.append(neighbor)

    # Step 2: Initialize distances
    distance = {node: float('inf') for node in topo_order}
    distance[start] = 0

    # Step 3: Relax edges
    for node in topo_order:
        for src, dest, weight in edges:
            if src == node and distance[src] + weight < distance[dest]:
                distance[dest] = distance[src] + weight

    return distance