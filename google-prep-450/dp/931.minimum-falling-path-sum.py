#
# @lc app=leetcode id=931 lang=python3
#
# [931] Minimum Falling Path Sum
#

# @lc code=start
class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        if len(matrix[0]) == 1:
            currRowMinPath = 0
            for i in range(len(matrix)):
                currRowMinPath += matrix[i][0]
            return currRowMinPath
        
        prevRowMinPath = [0]*len(matrix[0])
        for i in range(len(matrix)):
            currRowMinPath = []
            for j in range(len(matrix[0])):
                if j == 0:
                    currRowMinPath.append(matrix[i][j] + min(prevRowMinPath[j], prevRowMinPath[j+1]))
                elif j == len(matrix[0]) - 1:
                    currRowMinPath.append(matrix[i][j] + min(prevRowMinPath[j-1], prevRowMinPath[j]))
                else:
                    currRowMinPath.append(matrix[i][j] + min(prevRowMinPath[j-1], prevRowMinPath[j], prevRowMinPath[j+1]))

            prevRowMinPath = currRowMinPath[:]

        return min(currRowMinPath)
# @lc code=end

