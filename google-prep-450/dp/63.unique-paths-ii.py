#
# @lc app=leetcode id=63 lang=python3
#
# [63] Unique Paths II
#

# @lc code=start
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        """ This function returns number of paths to reach the bottom right cornor
            of a grid. It uses dynamic programming with bottoms up approach to achieve
            this.

            Args:
                obstacleGrid (List[List[int]]) : grid containg the obstacles in the path
            Returns:
                Number of ways to reach the end
        """

        nrows = len(obstacleGrid)
        ncols = len(obstacleGrid[0])

        ## no of ways to reach previous row is initalised as 0 bcoz we cant reach it and it 
        ## is hypothetical
        
        prevRowPaths = [0]*ncols 
        prevRowPaths[0] = 1
        ## iterate over each cell and come up with number of paths
        ## number of paths for each cell = path for cell directly at top + path for cell 
        ## right left to it.

        for i in range(nrows):
            currRowPaths = []
            for j in range(ncols):

                ## if there is an obstacle then the number of ways would be 0
                if obstacleGrid[i][j] == 1:
                    currRowPaths.append(0)
                else:

                    ## for first column we can only come from top
                    if j == 0:
                        currRowPaths.append(prevRowPaths[j])
                    else:
                        currRowPaths.append(prevRowPaths[j] + currRowPaths[j-1])


            ## update prevRowPaths
            prevRowPaths = currRowPaths[::]


        return currRowPaths[-1] 
                
        
# @lc code=end

