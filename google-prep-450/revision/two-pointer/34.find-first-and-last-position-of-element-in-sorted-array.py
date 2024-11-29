#
# @lc app=leetcode id=34 lang=python3
#
# [34] Find First and Last Position of Element in Sorted Array
#

# @lc code=start
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start = 0
        end = len(nums) - 1

        while start <= end:
            mid = (start + end)//2
            if nums[mid] >= target:
                end = mid - 1
            else:
                start = mid+1 

        startingPoint = start 

        start = 0
        end = len(nums) - 1

        while start <= end:
            mid = (start + end)//2
            if nums[mid] > target:
                end = mid -1 
            else:
                start = mid + 1

        endingPont = end 

        if startingPoint <= endingPont and nums[startingPoint] == target and 0 <= startingPoint < len(nums):
            return [startingPoint, endingPont]
        return [-1, -1]
        
# @lc code=end

