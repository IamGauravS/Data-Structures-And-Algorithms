#
# @lc app=leetcode id=673 lang=python3
#
# [673] Number of Longest Increasing Subsequence
#

# @lc code=start
class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        N = len(nums)
        lengths = [1] * N  # Store length of LIS ending at index i
        counts = [1] * N    # Store count of LISs ending at index i
        
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] > nums[j] and lengths[i] < lengths[j] + 1: ## if the new substring being formed is greater than curr substring
                    lengths[i] = lengths[j] + 1
                    counts[i] = counts[j]

                elif nums[i] > nums[j] and lengths[i] == lengths[j] + 1:
                    lengths[i] = lengths[j] + 1
                    counts[i] += counts[j]

        maxLength = max(lengths)
        totalCount = 0

        for i in range(len(lengths)):
            if lengths[i] == maxLength:
                totalCount += counts[i]

        return totalCount

    
        
# @lc code=end

