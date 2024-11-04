from collections import defaultdict, deque
from typing import List, Tuple

class Solution:
    def toposort(self, i, visited, topoSort):
        visited.add(i)

        for neighbor, _ in self.adjList[i]:
            if neighbor not in visited:
                self.toposort(neighbor, visited, topoSort)

        topoSort.append(i)


    def findShortestPath(self, n: int, edges: List[Tuple[int, int, int]], start: int) -> List[float]:

        self.adjList = defaultdict(list)
        

        for u, v, w in edges:
            self.adjList[u].append((v, w))

        topoSort = []
        visited = set()

        for i in range(n):
            if i not in visited:
                self.toposort(i, visited, topoSort)

        topoSort = topoSort[::-1]

        distances = [float('inf')]*n 
        distances[start] = 0

        for node in topoSort:
            if distances[node] != float('inf'):
                for neighbor, weight in self.adjList[node]:
                    if distances[node] + weight < distances[neighbor]:
                        distances[neighbor] = distances[node] + weight


        return distances


        
