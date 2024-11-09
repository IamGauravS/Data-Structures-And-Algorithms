#
# @lc app=leetcode id=120 lang=python3
#
# [120] Triangle
#

# @lc code=start
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        """
            This function uses bottoms up dynamic programming approach to return the minimum sum path
            to reach from top row to bottom row. For each cell the minimum path would be curr triangle
            cell value + minimum of i-1th and ith cell in column just above.

            Args:
                triangles List[List[int]] : triangle array
            Returns:
                minimumPathSum (int) : minimum path sum to reach last row
        """

        ## if triangle has only one element
        if len(triangle) == 1:
            return triangle[0][0]
        
        nrows = len(triangle)

        ## initialise prev row min path to first row
        prevRowMinPath = triangle[0]

        for i in range(1, nrows):
            currRowMinPath = []
            ## curr row will i+1 elements
            for j in range(i+1):
                ## since i-1 element is not available for 0th element
                if j == 0:
                    currRowMinPath.append(triangle[i][j] + prevRowMinPath[j])

                ## since there is no ith element in the row above so there is no path from there
                elif j == i:
                    currRowMinPath.append(triangle[i][j] + prevRowMinPath[j-1])

                else:
                    currRowMinPath.append(triangle[i][j] + min(prevRowMinPath[j-1], prevRowMinPath[j]))

            ## update pre
            prevRowMinPath = currRowMinPath[:]

        
        ## minimum path sum would be the minimum of path sums of last row
        minimumPathSum = min(currRowMinPath)

        return minimumPathSum
                  
        
# @lc code=end

