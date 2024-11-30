#
# @lc app=leetcode id=1901 lang=python3
#
# [1901] Find a Peak Element II
#

# @lc code=start
from typing import List

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        maxi = 0
        for i in range(1, len(nums)):
            if nums[i] > nums[maxi]:
                maxi = i

        return maxi
        

    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        if not mat or not mat[0]:
            return []

        nrows = len(mat)
        ncols = len(mat[0])

        low = 0
        high = nrows - 1

        while low <= high:
            mid = (low + high) // 2
            currPeak = self.findPeakElement(mat[mid])

            top = -1 
            bottom = -1

            if mid - 1 >= 0:
                top = mat[mid-1][currPeak]
            
            if mid + 1 < nrows:
                bottom = mat[mid + 1][currPeak]

            if (mat[mid][currPeak] > bottom) and ( mat[mid][currPeak] > top):
                return [mid, currPeak]
            
            elif mat[mid][currPeak] < top:
                high = mid - 1

            else:
                low = mid + 1


        return [-1, -1]

        
# @lc code=end

