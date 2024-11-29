#
# @lc app=leetcode id=88 lang=python3
#
# [88] Merge Sorted Array
#

# @lc code=start
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        totalLen = m + n

        nums1 = nums1

        ind1 = len(nums1) - 1 - n
        ind2 = len(nums2) - 1
        pointer = m + n - 1

        while ind1 >= 0 and ind2 >= 0:
            if nums1[ind1] >= nums2[ind2]:
                nums1[pointer] = nums1[ind1]
                pointer -= 1
                ind1 -= 1

            elif nums1[ind1] < nums2[ind2]:
                nums1[pointer] = nums2[ind2]
                pointer -= 1
                ind2 -= 1

        while ind2 >= 0:
            nums1[pointer] = nums2[ind2]
            ind2 -= 1
            pointer -= 1

        return 

        
        
# @lc code=end

