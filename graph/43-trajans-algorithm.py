class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[] for _ in range(vertices)]
        self.ids = [-1] * vertices  # To store the ids of the vertices
        self.low = [-1] * vertices  # To store the low-link values of the vertices
        self.on_stack = [False] * vertices  # To track whether a vertex is on the stack
        self.stack = []
        self.sccs = []

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def dfs(self, u, idx):
        self.ids[u] = idx
        self.low[u] = idx
        idx += 1
        self.stack.append(u)
        self.on_stack[u] = True

        for v in self.graph[u]:
            if self.ids[v] == -1:
                self.dfs(v, idx)
                self.low[u] = min(self.low[u], self.low[v])
            elif self.on_stack[v]:
                self.low[u] = min(self.low[u], self.ids[v])

        if self.low[u] == self.ids[u]:
            scc = []
            while True:
                v = self.stack.pop()
                self.on_stack[v] = False
                scc.append(v)
                if v == u:
                    break
            self.sccs.append(scc)

    def find_sccs(self):
        idx = 0
        for v in range(self.V):
            if self.ids[v] == -1:
                self.dfs(v, idx)


