#
# @lc app=leetcode id=1631 lang=python3
#
# [1631] Path With Minimum Effort
#

# @lc code=start
import heapq
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        nrows = len(heights)
        ncols = len(heights[0]) 

        distances = [[float('inf')] * ncols for _ in range(nrows)]

        distances[0][0] = 0
        priorityQueue = [(0,0,0)]
        delta = [(0,1), (1,0), (0,-1), (-1,0)]

        while priorityQueue:
            distance, curri, currj  = heapq.heappop(priorityQueue)

            if (curri, currj) == (nrows-1, ncols-1):
                return distance

            for dx, dy in delta:
                newi = curri + dx 
                newj = currj + dy 

                if 0 <= newi < nrows and 0 <= newj < ncols:
                    possibleDistance = max(distance, abs(heights[curri][currj] - heights[newi][newj]))
                    if possibleDistance < distances[newi][newj]:
                        distances[newi][newj] = possibleDistance
                        heapq.heappush(priorityQueue, (possibleDistance, newi, newj))


        return distances[-1][-1]


        
# @lc code=end

