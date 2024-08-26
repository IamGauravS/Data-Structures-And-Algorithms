class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        if len(nums) == 1: 
            return nums[0]
        
        if nums[0] != nums[1]:
            return nums[0]
    
        if nums[-1] != nums[-2]:
            return nums[-1]
        
        start = 1
        end = len(nums) - 2

        while start <= end:
            mid = start + (end - start) // 2

            if  nums[mid-1] != nums[mid] and  nums[mid] != nums[mid+1]:
                return nums[mid]
            
            if mid % 2 == 1:
                if nums[mid-1] == nums[mid]:
                    start = mid + 1
                else:
                    end = mid - 1

            else:
                if nums[mid] == nums[mid+1]:
                    start = mid + 1
                else:
                    end = mid - 1
                    

            


