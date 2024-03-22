class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_mult = [1 for i in range(len(nums))]
        
        curr = 1
        for i in range(1, len(nums)):
            curr = curr*nums[i-1]
            prefix_mult[i] = curr 
            
        
        curr = 1
        for i in range(len(nums)-2, -1, -1):
            curr = curr* nums[i+1]
            prefix_mult[i] = curr*prefix_mult[i]
            
        return prefix_mult 
            
            
        