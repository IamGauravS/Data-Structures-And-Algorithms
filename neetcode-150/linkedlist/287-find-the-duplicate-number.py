class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        i = 0
        while i < len(nums):
            if nums[i] != i + 1:
                j = nums[i] - 1  ## correct postion of nums[i]
                if nums[i] != nums[j]:
                    nums[i], nums[j] = nums[j], nums[i]  # swap
                else:
                    return nums[i]
            else:
                i += 1
                
                
                
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        slow, fast = 0, 0 
        
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]] ## we are advancing fast twice
            if slow == fast:
                break 
                
                
        slow2 = 0  ## second slow pointer 
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow
                
                
        