#
# @lc app=leetcode id=493 lang=python3
#
# [493] Reverse Pairs
#

# @lc code=start
class Solution:
    def mergeSort(self, nums, start, end):
        if end - start <= 1:
            return 0  # No reverse pairs in a single element or empty range

        mid = (start + end) // 2
        # Count reverse pairs in left, right, and across the halves
        count = self.mergeSort(nums, start, mid) + self.mergeSort(nums, mid, end)

        # Count reverse pairs across the two halves
        j = mid
        for i in range(start, mid):
            while j < end and nums[i] > 2 * nums[j]:
                j += 1
            count += j - mid

        # Merge step (standard merge sort)
        temp = []
        i, j = start, mid
        while i < mid and j < end:
            if nums[i] <= nums[j]:
                temp.append(nums[i])
                i += 1
            else:
                temp.append(nums[j])
                j += 1

        temp.extend(nums[i:mid])
        temp.extend(nums[j:end])
        nums[start:end] = temp  # Write back the sorted portion

        return count

    def reversePairs(self, nums: List[int]) -> int:
        return self.mergeSort(nums, 0, len(nums))

        
# @lc code=end

