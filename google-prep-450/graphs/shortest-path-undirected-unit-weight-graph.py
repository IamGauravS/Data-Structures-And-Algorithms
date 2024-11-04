from collections import deque

class Solution:
    def shortestPath(self, n, adjList, start):

        distance = [float('inf')]*n 

        queue = deque()
        queue.append(start)
        distance[start] = 0

        while queue:
            currNode = queue.popleft()

            for neighbor in adjList[currNode]:
                if distance[neighbor] == float('inf'):
                    distance[neighbor] = distance[currNode] + 1
                    queue.append(neighbor)


        return distance
