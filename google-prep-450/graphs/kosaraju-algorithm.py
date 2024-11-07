from collections import defaultdict
from typing import List

class Solution:
    
    # Function to find all strongly connected components in the graph.
    def kosaraju(self, V: int, adj: List[List[int]]) -> List[List[int]]:
        # Step 1: Do a DFS to get the finish order of nodes
        stack = []
        visited = [False] * V
        
        # First DFS to determine the finishing order
        for i in range(V):
            if not visited[i]:
                self.dfs(i, visited, stack, adj)
        
        # Step 2: Create a transposed graph
        transposed_adj = self.transpose_graph(V, adj)
        
        # Step 3: Process all nodes in order of their finish times in reverse order
        visited = [False] * V
        sccs = []  # List to store all SCCs
        
        while stack:
            node = stack.pop()
            if not visited[node]:
                # Collect nodes in the current SCC
                current_scc = []
                self.dfs_transposed(node, visited, transposed_adj, current_scc)
                sccs.append(current_scc)  # Add this SCC to the list of SCCs
        
        return sccs

    # Helper DFS function to fill the stack with nodes by finish order
    def dfs(self, v: int, visited: List[bool], stack: List[int], adj: List[List[int]]):
        visited[v] = True
        for neighbor in adj[v]:
            if not visited[neighbor]:
                self.dfs(neighbor, visited, stack, adj)
        stack.append(v)  # Push node to stack after all neighbors are visited

    # Function to transpose the graph (reverse all edges)
    def transpose_graph(self, V: int, adj: List[List[int]]) -> defaultdict:
        transposed_adj = defaultdict(list)
        for i in range(V):
            for neighbor in adj[i]:
                transposed_adj[neighbor].append(i)
        return transposed_adj

    # DFS on transposed graph to collect nodes in the same SCC
    def dfs_transposed(self, v: int, visited: List[bool], transposed_adj: defaultdict, current_scc: List[int]):
        visited[v] = True
        current_scc.append(v)  # Add node to the current SCC
        for neighbor in transposed_adj[v]:
            if not visited[neighbor]:
                self.dfs_transposed(neighbor, visited, transposed_adj, current_scc)
