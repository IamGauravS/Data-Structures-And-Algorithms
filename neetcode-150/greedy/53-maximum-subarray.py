class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxValue = -float('inf')
        currSum = 0
        for i in range(len(nums)):
            currSum += nums[i]
            if currSum < 0:
                currSum = 0
                maxValue = max(maxValue, nums[i])
            else:
                maxValue = max(maxValue, currSum)

        return maxValue