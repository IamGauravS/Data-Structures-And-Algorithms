from collections import deque
from typing import List

class Solution:
    def isCyclic(self, V: int, graph: List[List[int]]) -> bool:
        # Step 1: Calculate in-degrees of all vertices
        in_degree = [0] * V
        for u in range(V):
            for v in graph[u]:
                in_degree[v] += 1

        # Step 2: Initialize queue with nodes having in-degree 0
        queue = deque([i for i in range(V) if in_degree[i] == 0])
        
        # Step 3: Process nodes in topological order
        processed_count = 0
        while queue:
            node = queue.popleft()
            processed_count += 1

            # For each outgoing edge, reduce the in-degree of the neighbor
            for neighbor in graph[node]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        # Step 4: If processed nodes are less than total nodes, a cycle exists
        return processed_count != V  # True if cycle exists, False if not
