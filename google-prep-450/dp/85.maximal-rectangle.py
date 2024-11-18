#
# @lc app=leetcode id=85 lang=python3
#
# [85] Maximal Rectangle
#

# @lc code=start
class Solution:
    def maxHistogramSize(self, heights):
        stack = []
        maxArea = 0
        n = len(heights)

        ## add a sentinal height of 0 to flush out remaining bars
        heights.append(0)

        for i in range(len(heights)):
            while stack and heights[i] < heights[stack[-1]]:
                h = heights[stack.pop()]  # Height of the rectangle
                # Calculate width
                w = i if not stack else i - stack[-1] - 1
                maxArea = max(maxArea, h * w)

            stack.append(i)


        return maxArea


    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        heights = [0]*len(matrix[0])
        maxArea = 0
        for i in range(0, len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == "1":
                    heights[j] += 1
                else:
                    heights[j] = 0

            maxArea = max(maxArea, self.maxHistogramSize(heights))


        return maxArea


        
# @lc code=end

