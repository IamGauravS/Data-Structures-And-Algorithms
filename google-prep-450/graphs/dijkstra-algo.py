import heapq
from typing import List, Tuple

class Solution:
    def shortestPath(self, n: int, edges: List[Tuple[int, int, int]], source: int, target: int) -> int:
        adjList = {i: [] for i in range(n)}

        for src, tgt, weight in edges:
            adjList[src].append((tgt, weight))

        priorityQueue = []
        distance = [float('inf')] * n
        distance[source] = 0

        heapq.heappush(priorityQueue, (0, source))

        while priorityQueue:
            currDistance, node = heapq.heappop(priorityQueue)

            if node == target:
                return currDistance

            for neighbor, weight in adjList[node]:
                if weight + currDistance < distance[neighbor]:
                    distance[neighbor] = weight + currDistance
                    heapq.heappush(priorityQueue, (distance[neighbor], neighbor))

        return distance[target] if distance[target] != float('inf') else -1

# Example usage
