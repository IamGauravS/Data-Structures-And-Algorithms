#
# @lc app=leetcode id=368 lang=python3
#
# [368] Largest Divisible Subset
#

# @lc code=start
from collections import defaultdict
class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        dp = [1]*len(nums)
        ldsStore = defaultdict(list)
        nums.sort()
        for i in range(len(nums)):
            maxJ = -1
            for j in range(i):
                if dp[i] < 1 + dp[j] and (nums[i] % nums[j] == 0 or nums[j] % nums[i] == 0):
                    maxJ = j 
                    dp[i] = 1 + dp[j] 

            
            ldsStore[i] = ldsStore[maxJ][:] + [nums[i]]


        maxLds = dp.index(max(dp))
        return ldsStore[maxLds]
        
# @lc code=end

