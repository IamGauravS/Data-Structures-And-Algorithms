import sys
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currSum = 0
        maxSum = -sys.maxsize

        for i in range(len(nums)):
            currSum += nums[i]

            if maxSum < currSum:
                maxSum = currSum

            if currSum < 0:
                currSum = 0

        return maxSum
                
