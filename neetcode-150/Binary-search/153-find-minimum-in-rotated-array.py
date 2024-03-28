import sys
class Solution:
    def findMin(self, nums: List[int]) -> int:
        start = 0
        end = len(nums)-1
        min_element = sys.maxsize
        while start <= end:
            mid = (start+end)//2
            
            if nums[start] <= nums[mid]:  ## left half is sorted ## we right equal to for the case where there is one element
                min_element = min(nums[start], min_element)
                start = mid+1   ## here we wont be considering mid in future so we do mid+1 and mid-1
                
            else:  ## right half is sorted
                min_element = min(nums[mid], min_element)
                end = mid -1
                
        return min_element
                