#
# @lc app=leetcode id=778 lang=python3
#
# [778] Swim in Rising Water
#

# @lc code=start
import heapq
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        """
            This function uses a min heap to find the least time 
            we will take to reach (n-1, n-1) from (0,0). The time complexity
            for this algorithm is o(nlogn) 

            Args: 
                grid (ListList[int]]) : grid with water levels at t = 0

            Returns:
                minTime : minimum time to reach (n-1, n-1)
        """
        
        if not grid or not grid[0]:
            return 0
        
        nrows, ncols = len(grid), len(grid[0])

        ## if grid has only 1 element then we are alreaady at end
        if nrows == 1 and ncols == 1:
            return 0

        minHeap = [(grid[0][0],0,0)]  ## time, i, j
        visited = set()
        visited.add((0,0))  ## mark source as visited

        delta = [(0,1), (1,0), (0,-1), (-1,0)]  ## 4 directional movement
        minTime = -float('inf')

        while minHeap:
            currTime, curri, currj = heapq.heappop(minHeap)

            ## update minTime
            minTime = max(minTime, currTime)

            ## return currTime if we have reached the end
            if curri == nrows - 1 and currj == ncols - 1:
                return minTime 
            
            ## put all neighboring paths in the heap
            for dx, dy in delta:
                newi = curri + dx 
                newj = currj + dy 

                ## visit neighbors that are unvisited
                if 0 <= newi < nrows and 0 <= newj < ncols and (newi, newj) not in visited:
                    heapq.heappush(minHeap, (grid[newi][newj], newi, newj))
                    visited.add((newi, newj))  ## mark visited
            





# @lc code=end

