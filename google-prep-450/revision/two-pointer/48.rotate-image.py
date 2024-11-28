#
# @lc app=leetcode id=48 lang=python3
#
# [48] Rotate Image
#

# @lc code=start
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        l, r = 0 , len(matrix) -1
        
        while l < r:
            top, bottom = l, r 
            for i in range(r - l):
                
                ## save the top left value
                topLeft = matrix[top][l + i]

                ## move bottom left into top left
                matrix[top][l + i] = matrix[bottom - i][l]

                ## move bottom right into bottom left
                matrix[bottom - i][l] = matrix[bottom][r - i]

                ## move top right into bottom right
                matrix[bottom][r - i] = matrix[top + i][r]

                ## move top left into top right
                matrix[top + i][r] = topLeft 

            r -= 1 
            l += 1


        return matrix
        
# @lc code=end

