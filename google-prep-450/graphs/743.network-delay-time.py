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
        
        adjList = defaultdict(list)

        for u, v, w in times:
            adjList[u].append((v, w))

        distances = [float('inf')]*n
        distances[k-1] = 0

        priorityQueue = [(0, k)]

        while priorityQueue:
            currTime, currNode = heapq.heappop(priorityQueue)

            for neighbor, time in adjList[currNode]:
                if time + currTime < distances[neighbor-1]:
                    distances[neighbor-1] = time + currTime
                    heapq.heappush(priorityQueue, (distances[neighbor-1], neighbor))

        minTime = max(distances)

        return minTime if minTime != float('inf') else -1


        

# @lc code=end

