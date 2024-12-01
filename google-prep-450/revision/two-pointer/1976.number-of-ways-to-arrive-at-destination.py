#
# @lc app=leetcode id=1976 lang=python3
#
# [1976] Number of Ways to Arrive at Destination
#

# @lc code=start
from collections import defaultdict
import heapq

class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        MOD = 10**9 + 7
        
        # Initialize distance and number of ways arrays
        distance = [float('inf')] * n
        noOfWays = [0] * n
        
        # Build adjacency list
        adjList = defaultdict(list)
        for u, v, wt in roads:
            adjList[u].append((v, wt))
            adjList[v].append((u, wt))
        
        # Start from node 0
        distance[0] = 0
        noOfWays[0] = 1
        
        # Min-heap for Dijkstra's algorithm
        heap = [(0, 0)]  # (current_distance, current_node)
        
        while heap:
            currDist, currNode = heapq.heappop(heap)
            
            # Skip if a better distance has already been found
            if currDist > distance[currNode]:
                continue
            
            # Relax edges
            for neighbor, edgeWeight in adjList[currNode]:
                newDist = currDist + edgeWeight
                
                # Found a shorter path to neighbor
                if newDist < distance[neighbor]:
                    distance[neighbor] = newDist
                    noOfWays[neighbor] = noOfWays[currNode]
                    heapq.heappush(heap, (newDist, neighbor))
                
                # Found an additional shortest path to neighbor
                elif newDist == distance[neighbor]:
                    noOfWays[neighbor] = (noOfWays[neighbor] + noOfWays[currNode]) % MOD
        
        return noOfWays[-1]

        
# @lc code=end

