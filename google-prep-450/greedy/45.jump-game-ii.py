#
# @lc app=leetcode id=45 lang=python3
#
# [45] Jump Game II
#

# @lc code=start
class Solution:
    def jump(self, nums: List[int]) -> int:
        left, right = 0, 0
        noOfSteps = 0

        while right < len(nums)-1:
            fartherstRight = 0

            for i in range(left, right+1):
                fartherstRight = max(fartherstRight, nums[i]+i)

            left = right + 1
            right = fartherstRight
            noOfSteps += 1

        return noOfSteps
        
# @lc code=end

