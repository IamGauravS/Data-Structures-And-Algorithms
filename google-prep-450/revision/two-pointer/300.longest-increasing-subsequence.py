#
# @lc app=leetcode id=300 lang=python3
#
# [300] Longest Increasing Subsequence
#

# @lc code=start
import bisect
class Solution:
    def lengthOfLISV1(self, nums: List[int]) -> int:
        dp = [1]*len(nums)

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[j] > nums[i]:
                    dp[j] = max(dp[j], 1 + dp[i])


        return max(dp)
    
    

    def lengthOfLIS(self, nums: List[int]) -> int:
        sub = []  # List to store the smallest tail of all increasing subsequences
        for num in nums:
            # Find the position to replace or append using binary search
            pos = bisect.bisect_left(sub, num)
            if pos == len(sub):
                sub.append(num)  # Extend the subsequence
            else:
                sub[pos] = num  # Replace to maintain the smallest tail
        return len(sub)

        
# @lc code=end

