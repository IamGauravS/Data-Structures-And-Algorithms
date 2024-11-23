#
# @lc app=leetcode id=42 lang=python3
#
# [42] Trapping Rain Water
#

# @lc code=start
class Solution:
    def trap(self, height: List[int]) -> int:
        """
        calculate maximum water that can be trapped given a height map

        Args:
        height (List[int]) : height of each feature

        Returns:
        trappedWater (int) : water trapped between heights
        """

        if not isinstance(height, list) or any(h < 0 for h in height):
            raise ValueError("incorrect input")
        
        # Edge case: if height is empty or has only two height then no water will be trapped
        if len(height) <= 2:
            return 0
        
        left, right = 0, len(height) - 1
        left_max, right_max = 0, 0
        trapped_water = 0

        while left < right:
            if height[left] < height[right]:
                if height[left] >= left_max:
                    left_max = height[left]
                else:
                    trapped_water += left_max - height[left]
                left += 1
            else:
                if height[right] >= right_max:
                    right_max = height[right]
                else:
                    trapped_water += right_max - height[right]
                right -= 1

        return trapped_water

        
# @lc code=end

