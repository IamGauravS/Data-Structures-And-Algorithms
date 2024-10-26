class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
       
        maxRange = 0
        for i in range(len(nums)):
            if maxRange >= i:
                newRange = i + nums[i]
                maxRange = max(newRange, maxRange)

            else:
                return False 

        return True