#
# @lc app=leetcode id=743 lang=python3
#
# [743] Network Delay Time
#

# @lc code=start
from collections import defaultdict
import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        distArray = [float('inf')]*n 
        adjList = defaultdict(list)

        for src, dest, dist in times:
            adjList[src-1].append((dest-1, dist))

        distArray[k-1] = 0
        heap = [(0, k-1)]

        while heap:
            currDist, node = heapq.heappop(heap)

            for neighbor, dist in adjList[node]:
                if currDist + dist < distArray[neighbor]:
                    distArray[neighbor] = currDist + dist 
                    heapq.heappush(heap, (distArray[neighbor], neighbor))

        if any(dist == float('inf') for dist in distArray):
            return -1
        return max(distArray)




        
# @lc code=end

