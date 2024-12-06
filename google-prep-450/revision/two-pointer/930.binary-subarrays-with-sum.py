#
# @lc app=leetcode id=930 lang=python3
#
# [930] Binary Subarrays With Sum
#

# @lc code=start
class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        
        def helper(x):
            if x < 0:
                return 0
            
            l, count = 0, 0
            currSum = 0

            for r in range(len(nums)):
                currSum += nums[r]
                while currSum > x:
                    currSum -= nums[l]
                    l += 1

                count += (r-l+1)


            return count 

        return helper(goal) - helper(goal-1)


        
# @lc code=end

