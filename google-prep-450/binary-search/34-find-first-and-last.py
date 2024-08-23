from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def findFirst(nums, target):
            start, end = 0, len(nums) - 1
            while start <= end:
                mid = (start + end) // 2
                if nums[mid] < target:
                    start = mid + 1
                else:
                    end = mid - 1
            return start

        def findLast(nums, target):
            start, end = 0, len(nums) - 1
            while start <= end:
                mid = (start + end) // 2
                if nums[mid] <= target:
                    start = mid + 1
                else:
                    end = mid - 1
            return end

        first = findFirst(nums, target)
        last = findLast(nums, target)

        if first <= last and first < len(nums) and nums[first] == target:
            return [first, last]
        else:
            return [-1, -1]

