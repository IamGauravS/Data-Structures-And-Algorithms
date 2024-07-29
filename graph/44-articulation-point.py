class Graph:
    def __init__(self, vertices):
        self.V = vertices  # Number of vertices
        self.adj_list = [[] for _ in range(vertices)]  # Adjacency list
        self.visited = [False] * vertices  # Track visited vertices
        self.discovery_time = [-1] * vertices  # Discovery times of vertices
        self.low_link = [-1] * vertices  # Low-link values of vertices
        self.time = 0  # Global time counter for DFS
        self.articulation_points = set()  # Set to store articulation points

    def add_edge(self, u, v):
        # Add an undirected edge between u and v
        self.adj_list[u].append(v)
        self.adj_list[v].append(u)

    def find_articulation_points(self):
        # Perform DFS on all unvisited vertices
        for v in range(self.V):
            if not self.visited[v]:
                self._dfs_articulation_points(v, -1)

    def _dfs_articulation_points(self, u, parent):
        children = 0  # Count of u's children
        self.visited[u] = True  # Mark u as visited
        self.discovery_time[u] = self.time  # Set discovery time
        self.low_link[u] = self.time  # Set low-link value
        self.time += 1  # Increment global time

        # Visit all neighbors v of u
        for v in self.adj_list[u]:
            if not self.visited[v]:  # v is not visited
                children += 1
                self._dfs_articulation_points(v, u)  # DFS on v
                self.low_link[u] = min(self.low_link[u], self.low_link[v])  # Update low-link of u

                # u is an articulation point in following cases:
                # (1) u is root of DFS tree and has two or more children.
                # (2) u is not root of DFS tree and low value of one of its child is more than discovery value of u.
                if parent != -1 and self.low_link[v] >= self.discovery_time[u]:
                    self.articulation_points.add(u)

            elif v != parent:  # Update low value of u for parent function calls.
                self.low_link[u] = min(self.low_link[u], self.discovery_time[v])

        # If u is the root node in DFS tree and has two or more children.
        if parent == -1 and children > 1:
            self.articulation_points.add(u)