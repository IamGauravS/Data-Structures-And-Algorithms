#
# @lc app=leetcode id=240 lang=python3
#
# [240] Search a 2D Matrix II
#

# @lc code=start
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        startRow = len(matrix) - 1
        startCol = 0

        while startCol < len(matrix[0]) and startRow >= 0:
            if matrix[startRow][startCol] > target:
                startRow -= 1
            elif matrix[startRow][startCol] < target:
                startCol += 1

            else:
                return True 

        return False 
                
        
# @lc code=end

