class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) -1 
        
        while start <= end:
            mid = (start+end)//2
            
            if nums[mid] == target:
                return mid
            
            if nums[start] <= nums[mid]:  ## left is sorted
                if target < nums[mid] and target >= nums[start]:
                    end = mid -1 
                else:
                    start = mid + 1
                    
            else:  ## right is sorted 
                if target > nums[mid] and target <= nums[end]:
                    start = mid+1 
                else:
                    end = mid -1 
                    
        return -1
                