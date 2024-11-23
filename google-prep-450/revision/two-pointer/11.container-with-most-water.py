#
# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
#

# @lc code=start
from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        Returns the container with max possible water. It uses a monotonic stack to achieve this. 

        Args:
        height (List[int]) : height array

        Returns:
        maxWaterVolumn (int) : max water volume that a container can hold

        """
        # Edge case : if height array is empty or only has one height then we can containing
        if len(height) <= 1:
            return 0
        
        maxArea = 0

        left = 0
        right = len(height) - 1 

        while left < right:
            ## reduce the side with less height
            area = (right - left) * min(height[right], height[left])
            maxArea = max(maxArea, area)

            if height[right] < height[left]:
                right -= 1
            else:
                left += 1

        return maxArea

        
# @lc code=end

