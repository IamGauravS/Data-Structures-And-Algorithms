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

            for neighbor, weight in adjList[node]:
                if weight + currDistance < distance[neighbor]:
                    distance[neighbor] = weight + currDistance
                    heapq.heappush(priorityQueue, (distance[neighbor], neighbor))

        return distance
# Example usage

## 2. distance to a target we do early stopping
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

# 3. get path to target

import heapq
from typing import List, Tuple

class Solution:
    def shortestPath(self, n: int, edges: List[Tuple[int, int, int]], source: int, target: int) -> Tuple[int, List[int]]:
        # Build adjacency list
        adjList = {i: [] for i in range(n)}
        for src, tgt, weight in edges:
            adjList[src].append((tgt, weight))

        # Priority queue and distance tracking
        priorityQueue = []
        distance = [float('inf')] * n
        distance[source] = 0
        
        # Parent dictionary to reconstruct the path
        parent = {source: None}
        
        heapq.heappush(priorityQueue, (0, source))

        while priorityQueue:
            currDistance, node = heapq.heappop(priorityQueue)

            # If we reached the target node, no need to process further
            if node == target:
                break

            for neighbor, weight in adjList[node]:
                if weight + currDistance < distance[neighbor]:
                    distance[neighbor] = weight + currDistance
                    parent[neighbor] = node  # Track the path
                    heapq.heappush(priorityQueue, (distance[neighbor], neighbor))

        # If the target is unreachable, return inf distance and empty path
        if distance[target] == float('inf'):
            return float('inf'), []

        # Reconstruct path from source to target
        path = []
        curr = target
        while curr is not None:
            path.append(curr)
            curr = parent.get(curr)
        path.reverse()  # Reverse to get path from source to target

        return distance[target], path
