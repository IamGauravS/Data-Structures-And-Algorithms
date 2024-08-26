import sys
from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        currSmallest = sys.maxsize

        start = 0
        end = len(nums) - 1

        while start <= end:
            mid = (start + end) // 2

            if nums[mid] < currSmallest:
                currSmallest = nums[mid]

            if nums[mid] < nums[end]:
                end = mid - 1

            else:
                start = mid + 1



        return currSmallest
    
