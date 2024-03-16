import heapq

def prims_algorithm(edges, no_of_nodes):
    # Create an adjacency list
    adj = [[] for _ in range(no_of_nodes)]
    for src, dest, wt in edges:
        adj[src].append((wt, src, dest))  # Only add edges for the given direction
    
    heap = []
    visited = [False] * no_of_nodes

    # Choose an arbitrary node to start, here we choose node 0
    visited[0] = True
    for edge in adj[0]:
        heapq.heappush(heap, edge)

    output = []
    while heap:
        wt, src, dest = heapq.heappop(heap)
        
        if not visited[dest]:
            visited[dest] = True
            output.append((src, dest, wt))  # Append the edge and its weight
            for edge_next in adj[dest]:
                if not visited[edge_next[2]]:
                    heapq.heappush(heap, edge_next)
    
    return output

