#
# @lc app=leetcode id=45 lang=python3
#
# [45] Jump Game II
#

# @lc code=start
class Solution:
    def jump(self, nums: List[int]) -> int:
        
        if len(nums) <= 1:
            return 0
        
        jumps = 0
        currentEnd = 0
        farthest = 0

        for i in range(len(nums)-1):
            farthest = max(farthest, i+nums[i])

            if i == currentEnd:
                jumps += 1
                currentEnd = farthest
                if currentEnd >= len(nums)-1:
                    break 

        return jumps

        
# @lc code=end



