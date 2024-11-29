#
# @lc app=leetcode id=81 lang=python3
#
# [81] Search in Rotated Sorted Array II
#

# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        start = 0
        end = len(nums) - 1

        while start <= end:
            mid = (start + end)//2

            if nums[mid] == target:
                return True
            
            while start < mid and nums[start] == nums[mid]:
                start += 1
            while end > mid and nums[end] == nums[mid]:
                end -= 1
            
            ## right side is sorted
            if nums[start] <= nums[mid]:
                ## equal condition only on start side bcoz if it was equal to mid we would already have returned
                if nums[start] <= target < nums[mid]:
                    end = mid - 1
                else:
                    start = mid + 1

            ## left side is sorted
            else:
                ## check in left bounds
                if nums[mid] < target <= nums[end]:
                    start = mid + 1
                else:
                    end = mid - 1

        return False 
                    
        
# @lc code=end

