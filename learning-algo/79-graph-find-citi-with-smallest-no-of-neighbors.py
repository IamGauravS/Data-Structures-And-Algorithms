
import sys

def find_city(edges, no_of_vertices, treshold):
    dist = [[sys.maxsize for i in range(no_of_vertices)] for j in range(no_of_vertices)]

    for i in range(no_of_vertices):
            dist[i][i] = 0

    for edge in edges:
        dist[edge[0]][edge[1]] = edge[2]

    for k in range(no_of_vertices):
        for i in range(no_of_vertices):
            for j in range(no_of_vertices):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]


    cities = [0 for i in range(no_of_vertices)]
    for i in range(no_of_vertices):
        for j in range(no_of_vertices):
            if dist[i][j] <= treshold:
                cities[i] = cities[i]+1

    min_value = min(cities)
    return max(i for i, j in enumerate(cities) if j == min_value)
    