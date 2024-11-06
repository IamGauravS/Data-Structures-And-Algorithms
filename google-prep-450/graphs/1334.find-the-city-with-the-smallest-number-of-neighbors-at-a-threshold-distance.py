#
# @lc app=leetcode id=1334 lang=python3
#
# [1334] Find the City With the Smallest Number of Neighbors at a Threshold Distance
#

# @lc code=start
from typing import List

class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        """
        Find the city with the least number of neighboring cities within a given distance threshold.
        
        Uses the Floyd-Warshall algorithm to calculate shortest paths between all city pairs.
        
        Args:
        - n (int): Number of cities
        - edges (List[List[int]]): List of edges where each edge is represented as [source, destination, weight]
        - distanceThreshold (int): Maximum distance to consider for neighboring cities

        Returns:
        - int: The city with the least number of neighbors within the distance threshold
        """
        
        # Edge case: If there are no cities, return -1 (invalid input for this problem)
        if n == 0:
            return -1
        
        # Initialize distances to infinity, with 0 for self-distances
        distances = [[float('inf')] * n for _ in range(n)]
        for i in range(n):
            distances[i][i] = 0

        # Set initial distances based on direct edges
        for src, dest, weight in edges:
            distances[src][dest] = weight
            distances[dest][src] = weight  # Assuming the graph is undirected

        # Floyd-Warshall algorithm to find shortest paths between all pairs of cities
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    distances[i][j] = min(distances[i][j], distances[i][k] + distances[k][j])

        # Determine the city with the fewest neighbors within the distance threshold
        minNeighborCount = n  # Initialize to maximum possible number of cities
        bestCity = -1  # Variable to store the best city index
        
        for i in range(n):
            neighborCount = 0  # Count of cities within the distance threshold for city i
            
            # Count all reachable cities within the threshold for city i
            for j in range(n):
                if i != j and distances[i][j] <= distanceThreshold:
                    neighborCount += 1

            # Update best city if this city has fewer neighbors or if there's a tie with a higher city index
            if neighborCount < minNeighborCount or (neighborCount == minNeighborCount and i > bestCity):
                minNeighborCount = neighborCount
                bestCity = i

        return bestCity


        
# @lc code=end

