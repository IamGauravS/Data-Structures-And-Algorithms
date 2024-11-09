#
# @lc app=leetcode id=64 lang=python3
#
# [64] Minimum Path Sum
#

# @lc code=start
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        """
            This function returns the minimum path sum to the bottom right cornor
            of the grid starting from (0,0). We use dynamic programming approach filling
            the table bottoms up with curr cell value = min(cell just above, cell just left) + value
            of current cell

            Args:
                grid (List[List[int]]) : grid containg cost for each cell
            Returns:
                minimum path sum to reach the last cell
        """

        nrows = len(grid)
        ncols = len(grid[0])

        ## initialise to infinity as there are no valid path
        prevRowPathSum = [float('inf')]*ncols 
        prevRowPathSum[0] = 0

        for i in range(nrows):
            currRowPathSum = []
            for j in range(ncols):
                ## for first col we only have one way from top
                if j == 0:
                    currRowPathSum.append(prevRowPathSum[j] + grid[i][j])
                else:
                    currRowPathSum.append(grid[i][j] + min(prevRowPathSum[j], currRowPathSum[j-1]))

            ## update prevRowPathSum
            prevRowPathSum = currRowPathSum[:]


        return currRowPathSum[-1]



        
# @lc code=end

