#
# @lc app=leetcode id=2104 lang=python3
#
# [2104] Sum of Subarray Ranges
#

# @lc code=start
class Solution:
    def sumSubarrayMins(self, nums):
        subarraySum = 0
        stack = []

        for i in range(len(nums)+1):

            while stack and (i == len(nums) or nums[stack[-1]] >= nums[i]):
                curr = stack.pop()
                leftRange = -1 if not stack else stack[-1]
                rightRange = i
                count = (curr - leftRange)*(rightRange - curr)
                subarraySum += count*nums[curr]

            stack.append(i)

        return subarraySum

    def sumSubarrayMax(self, nums):
        subarraySum = 0
        stack = []

        for i in range(len(nums)+1):

            while stack and (i == len(nums) or nums[stack[-1]] <= nums[i]):
                curr = stack.pop()
                leftRange = -1 if not stack else stack[-1]
                rightRange = i
                count = (curr - leftRange)*(rightRange - curr)
                subarraySum += count*nums[curr]

            stack.append(i)

        return subarraySum
                



    def subArrayRanges(self, nums: List[int]) -> int:
        
        minSum = self.sumSubarrayMins(nums)
        maxSum = self.sumSubarrayMax(nums)

        return maxSum - minSum
        
# @lc code=end

