class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        numsSum = sum(nums)

        if numsSum % 2 == 1:
            return False
        
        targetSum = numsSum // 2

        dp = set()
        dp.add(0)

        for i in range(nums):
            nextDP = set()
            for t in dp:
                if t + nums[i] == targetSum:
                    return True 
                nextDP.add(t+nums[i])
                nextDP.add(t)   ## add previous dp value

            dp = nextDP 

        return True if targetSum in dp else False
            

        