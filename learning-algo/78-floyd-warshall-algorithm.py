##The Floyd-Warshall algorithm has a space complexity of O(|V|^2), as it needs to store the shortest distances between all pairs of vertices
## if it is undirected graph split it into dual edge
## matrix[i][j] =min(matrix[i][j], matrix[i ][k]+matrix[k][j]), where i = source node, j = destination node, and k = the node via which we are reaching from i to j
import sys
def ford_warshall_algorithm(edges, no_of_vertices):
    
    dist = [[sys.maxsize for i in range(no_of_vertices)] for j in range(no_of_vertices)]

    for i in range(no_of_vertices):
        for j in range(no_of_vertices):
            if i==j:
                dist[i][j] = 0

    for edge in edges:
        dist[edge[0]][edge[1]] = edge[2]

    ##The outer loop over each vertex k is the main part of the algorithm. For each pair of vertices i and j, it checks if the direct path from i to j is shorter or the path from i to k to j is shorter, and updates dist[i][j] and pred[i][j] accordingly.
    for k in range(no_of_vertices):
        for i in range(no_of_vertices):
            for j in range(no_of_vertices):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    return dist 