#
# @lc app=leetcode id=4 lang=python3
#
# [4] Median of Two Sorted Arrays
#

# @lc code=start
from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        ## nums1 should be shorter array
        if len(nums2) < len(nums1):
            nums1, nums2 = nums2, nums1

        lenA = len(nums1)
        lenB = len(nums2)

        halfLen = (lenA + lenB)//2
        left = 0
        right = lenA 

        while left <= right:
            partationA = (left+right)//2
            partationB = halfLen - partationA

            maxLeftA = -float('inf') if partationA == 0 else nums1[partationA-1] 
            minRightA = float('inf') if partationA == lenA else nums1[partationA]

            maxLeftB = -float('inf') if partationB == 0 else nums2[partationB-1]
            minRightB = float('inf') if partationB == lenB else nums2[partationB]

            if maxLeftA <= minRightB and maxLeftB <= minRightA:
                if (lenA+lenB)%2 == 0:
                    return (max(maxLeftA, maxLeftB) + min(minRightA, minRightB))/2
                else:
                    return min(minRightA, minRightB)

            elif maxLeftA > minRightB:
                right = partationA - 1
            else:
                left = partationA + 1 

        return -1
            








        
# @lc code=end

