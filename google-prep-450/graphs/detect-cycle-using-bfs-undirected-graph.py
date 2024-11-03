from collections import deque
from typing import List

class Solution:
    # Function to detect cycle in an undirected graph.
    def checkIfCycle(self, curr):
        queue = deque()
        queue.append((curr, None))  # node, parent
        self.visited.add(curr)

        while queue:
            curr, parent = queue.popleft()

            for neighbor in self.adj[curr]:
                if neighbor != parent:
                    if neighbor in self.visited:
                        return True  # Cycle detected
                    else:
                        queue.append((neighbor, curr))
                        self.visited.add(neighbor)

        return False

    def isCycle(self, V: int, adj: List[List[int]]) -> bool:
        # Code here
        self.visited = set()
        self.adj = adj

        for i in range(V):
            if i not in self.visited:
                if self.checkIfCycle(i):
                    return True

        return False