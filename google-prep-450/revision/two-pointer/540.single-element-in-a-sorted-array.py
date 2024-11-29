#
# @lc app=leetcode id=540 lang=python3
#
# [540] Single Element in a Sorted Array
#

# @lc code=start
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return nums[0]
        
        start = 0
        end = len(nums)-1


        while start <= end:
            mid = (start + end)//2

            if (mid == 0 and nums[mid] != nums[mid+1]) or (mid == len(nums)-1 and nums[mid] != nums[mid-1]):
                return nums[mid]

            if nums[mid] != nums[mid-1] and nums[mid] != nums[mid+1]:
                return nums[mid]

            if mid % 2 == 1:
                if nums[mid] != nums[mid -1]:
                    end = mid 
                else:
                    start = mid + 1

            else:
                if nums[mid] != nums[mid+1]:
                    end = mid 
                else:
                    start = mid + 1 


        return -1

        
# @lc code=end

