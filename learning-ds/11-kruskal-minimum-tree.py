class DisjointSet:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Path compression
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x != root_y:
            # Union by rank to optimize the tree height
            if self.rank[root_x] < self.rank[root_y]:
                self.parent[root_x] = root_y
            elif self.rank[root_x] > self.rank[root_y]:
                self.parent[root_y] = root_x
            else:
                self.parent[root_x] = root_y
                self.rank[root_y] += 1

            print(self.parent)
            print(self.rank)

def kruskal(graph):
    # Create a mapping of node names to integers
    node_to_int = {node: i for i, node in enumerate(graph)}
    int_to_node = {i: node for i, node in enumerate(graph)}

    edges = []
    for node in graph:
        for neighbor, weight in graph[node]:
            # Use the integer identifiers for the nodes
            edges.append((weight, node_to_int[node], node_to_int[neighbor]))

    edges.sort()

    num_vertices = len(graph)
    ds = DisjointSet(num_vertices)
    mst = []

    for edge in edges:
        weight, node, neighbor = edge
        if ds.find(node) != ds.find(neighbor):
            ds.union(node, neighbor)
            # Store the original node names in the MST
            mst.append((weight, int_to_node[node], int_to_node[neighbor]))

    return mst
# Example usage:
graph = {
    'A': [('B', 1), ('D', 4)],
    'B': [('A', 1), ('D', 2), ('E', 3)],
    'C': [('E', 5)],
    'D': [('A', 4), ('B', 2), ('E', 1)],
    'E': [('B', 3), ('C', 5), ('D', 1)]
}

minimum_spanning_tree = kruskal(graph)
print("Minimum Spanning Tree (Kruskal's Algorithm):", minimum_spanning_tree)
