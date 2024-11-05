#
# @lc app=leetcode id=1976 lang=python3
#
# [1976] Number of Ways to Arrive at Destination
#

# @lc code=start
from collections import defaultdict
import heapq
from typing import List

class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        MOD = 10**9 + 7
        adjList = defaultdict(list)

        for src, dest, time in roads:
            adjList[src].append((dest, time))
            adjList[dest].append((src, time))  # Assuming roads are bidirectional
            
        noOfWays = [0] * n
        totalTimes = [float('inf')] * n 

        noOfWays[0] = 1
        totalTimes[0] = 0

        priorityQueue = [(0, 0)]  # (time, city)

        while priorityQueue:
            currTime, city = heapq.heappop(priorityQueue)

            # If the current time is greater than the best-known time, skip
            if currTime > totalTimes[city]:
                continue

            for neighbor, time in adjList[city]:
                newTime = currTime + time
                if newTime < totalTimes[neighbor]:
                    totalTimes[neighbor] = newTime
                    noOfWays[neighbor] = noOfWays[city]
                    heapq.heappush(priorityQueue, (totalTimes[neighbor], neighbor))
                elif newTime == totalTimes[neighbor]:  # Use `elif` to avoid double-counting
                    noOfWays[neighbor] = (noOfWays[neighbor] + noOfWays[city]) % MOD

        return noOfWays[-1]

        
# @lc code=end

from collections import defaultdict
import heapq
from typing import List, Tuple

class Solution:
    def countPaths(self, n: int, roads: List[Tuple[int, int, int]]) -> int:
        """
        Given an undirected, weighted graph represented by 'roads' with 'n' nodes, 
        calculates the number of distinct shortest paths from node 0 to node n-1.

        Uses Dijkstra's algorithm with a priority queue to track minimum path distances,
        while also counting the number of distinct shortest paths reaching each node.

        Args:
        - n (int): The number of nodes in the graph.
        - roads (List[Tuple[int, int, int]]): Each tuple contains (src, dest, time),
          where time is the weight of the edge between src and dest.

        Returns:
        - int: The number of distinct shortest paths from node 0 to node n-1, 
          modulo 10^9 + 7.
        """

        MOD = 10**9 + 7

        # Edge case: if there's only one node, there's one trivial path (node 0 to node 0).
        if n == 1:
            return 1

        # Initialize adjacency list to represent the graph
        adjList = defaultdict(list)
        for src, dest, time in roads:
            adjList[src].append((dest, time))
            adjList[dest].append((src, time))  # Roads are bidirectional

        # Initialize path count and shortest path distance arrays
        noOfWays = [0] * n
        totalTimes = [float('inf')] * n
        noOfWays[0] = 1  # Start with one way to reach the starting node
        totalTimes[0] = 0  # Distance to the start node itself is 0

        # Priority queue to hold the minimum distance nodes (Dijkstra's algorithm)
        priorityQueue = [(0, 0)]  # (current_distance, node)

        # Process nodes in the priority queue
        while priorityQueue:
            currTime, city = heapq.heappop(priorityQueue)

            # Skip processing if we already have a shorter path to this node
            if currTime > totalTimes[city]:
                continue

            # Update neighbors with potential shorter paths
            for neighbor, time in adjList[city]:
                newTime = currTime + time
                if newTime < totalTimes[neighbor]:  # Found a shorter path
                    totalTimes[neighbor] = newTime
                    noOfWays[neighbor] = noOfWays[city]
                    heapq.heappush(priorityQueue, (newTime, neighbor))
                elif newTime == totalTimes[neighbor]:  # Found an equally short path
                    noOfWays[neighbor] = (noOfWays[neighbor] + noOfWays[city]) % MOD

        # Return the number of ways to reach the last node
        return noOfWays[n - 1]
