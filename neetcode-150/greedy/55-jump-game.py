class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxStep = nums[0] 
        lenNums = len(nums)
        for i in range(1, lenNums):
            if i <= maxStep:
                maxStep = max(maxStep, i+nums[i])
                if maxStep >= lenNums-1:
                    return True 
            else:
                return False 

        return maxStep >= lenNums -1