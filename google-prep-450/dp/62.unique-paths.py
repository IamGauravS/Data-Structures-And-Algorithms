#
# @lc app=leetcode id=62 lang=python3
#
# [62] Unique Paths
#

# @lc code=start
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        """
            This function return number of ways by which we can reach the last cell
            of m*n grid when we can only move in two directions either down or right.
            We use a dynamic programming based approach and fill the table bottoms up.

            Args:
                m (int) : no of rows
                n (int) : no of cols
            Returns:
                noOfWays (int) : max number of ways to reach the last cell
        """
        ## if there is only one row or column then there would be only one way to reach the end cell
        if m == 0 or n ==0:
            return 0
        
        if m == 1 or n == 1:
            return 1
        
        ## we initialise this to a arrary of size [1]*n because the first row will have only 1 way
        ## for each cell
        prevRowWays = [1]*n
        
        for i in range(1, m):
            currRowWays = [] ## variable to store no of ways for current row
            
            ## for the first cell in each row we can only come from top
            currRowWays.append(prevRowWays[0])
            for j in range(1, n):
                ## add number of ways from top and left
                currRowWays.append(prevRowWays[j]+currRowWays[j-1])

            ## update prevRowWays to currRowways for next iteration
            prevRowWays = currRowWays[::]


        return currRowWays[-1]

        
# @lc code=end

