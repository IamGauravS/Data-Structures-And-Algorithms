#
# @lc app=leetcode id=787 lang=python3
#
# [787] Cheapest Flights Within K Stops
#

# @lc code=start
from collections import defaultdict
import heapq
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adjList = defaultdict(list)

        for source, dest, price in flights:
            adjList[source].append((dest, price))

        distances = [float('inf')]*n 

        priorityQueue = [(0, 0, src)]
        distances[src] = 0

        while priorityQueue:
            noOfStops, cost, currNode = heapq.heappop(priorityQueue)

            if noOfStops == k+1:
                continue

            for neighbor, price in adjList[currNode]:
                if cost + price < distances[neighbor]:
                    distances[neighbor] = cost + price 
                    heapq.heappush(priorityQueue, (noOfStops+1, distances[neighbor], neighbor))

        return distances[dst] if distances[dst] != float('inf') else -1

        

        
# @lc code=end

