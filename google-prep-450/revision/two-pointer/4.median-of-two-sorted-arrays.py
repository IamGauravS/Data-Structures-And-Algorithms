#
# @lc app=leetcode id=4 lang=python3
#
# [4] Median of Two Sorted Arrays
#

# @lc code=start
from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Ensure nums1 is the shorter array
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        lenA, lenB = len(nums1), len(nums2)
        totalLen = lenA + lenB
        halfLen = totalLen // 2

        left, right = 0, lenA

        while left <= right:
            partitionA = (left + right) // 2
            partitionB = halfLen - partitionA

            maxLeftA = float('-inf') if partitionA == 0 else nums1[partitionA - 1]
            minRightA = float('inf') if partitionA == lenA else nums1[partitionA]

            maxLeftB = float('-inf') if partitionB == 0 else nums2[partitionB - 1]
            minRightB = float('inf') if partitionB == lenB else nums2[partitionB]

            # Valid partition
            if maxLeftA <= minRightB and maxLeftB <= minRightA:
                # Total length is even
                if totalLen % 2 == 0:
                    return (max(maxLeftA, maxLeftB) + min(minRightA, minRightB)) / 2
                # Total length is odd
                else:
                    return max(maxLeftA, maxLeftB)
            
            # Adjust search range
            elif maxLeftA > minRightB:
                right = partitionA - 1
            else:
                left = partitionA + 1

        raise ValueError("Input arrays are not sorted or invalid.")



        
# @lc code=end

1,4,5,6,7,9
2,3,8