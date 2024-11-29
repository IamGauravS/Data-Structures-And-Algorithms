#
# @lc app=leetcode id=152 lang=python3
#
# [152] Maximum Product Subarray
#

# @lc code=start
from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0

        maxProduct = nums[0]
        maxProductEndingHere = nums[0]
        minProductEndingHere = nums[0]

        for i in range(1, len(nums)):
            num = nums[i]

            if num < 0:
                # Swap max and min when the current number is negative
                maxProductEndingHere, minProductEndingHere = minProductEndingHere, maxProductEndingHere

            # Update max and min products ending at current index
            maxProductEndingHere = max(num, maxProductEndingHere * num)
            minProductEndingHere = min(num, minProductEndingHere * num)

            # Update the global maximum product
            maxProduct = max(maxProduct, maxProductEndingHere)

        return maxProduct
        
# @lc code=end

