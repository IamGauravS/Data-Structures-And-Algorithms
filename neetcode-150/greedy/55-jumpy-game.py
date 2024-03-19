class Solution:
    def canJump(self, nums: List[int]) -> bool:
        curr = 0
        maxi = nums[curr]
        
        while True:
            if maxi >= len(nums) -1:
                return True 
            if curr+1 <= maxi:
                curr = curr + 1
                jump = curr + nums[curr]
                if jump > maxi:
                    maxi = jump 
                    
            else:
                return False 