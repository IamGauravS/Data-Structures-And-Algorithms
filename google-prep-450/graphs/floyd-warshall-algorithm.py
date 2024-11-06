import sys

def floyd_warshall(graph):
    # Number of vertices
    V = len(graph)
    
    # Initialize distance matrix
    dist = [[sys.maxsize] * V for _ in range(V)]
    
    # Set up initial distances based on input graph
    for i in range(V):
        for j in range(V):
            if i == j:
                dist[i][j] = 0
            elif graph[i][j] != 0:
                dist[i][j] = graph[i][j]
    
    # Apply Floyd-Warshall algorithm
    for k in range(V):
        for i in range(V):
            for j in range(V):
                # Update the distance to be the minimum distance from i to j through k
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    
    # Check for negative cycles
    for i in range(V):
        if dist[i][i] < 0:
            print("Negative cycle detected")
            return None
    
    return dist

# Example usage:
graph = [
    [0, 3, sys.maxsize, 7],
    [8, 0, 2, sys.maxsize],
    [5, sys.maxsize, 0, 1],
    [2, sys.maxsize, sys.maxsize, 0]
]

result = floyd_warshall(graph)
if result:
    print("Shortest distance matrix:")
    for row in result:
        print(row)
