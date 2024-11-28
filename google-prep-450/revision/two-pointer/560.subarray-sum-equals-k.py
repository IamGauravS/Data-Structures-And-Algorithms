#
# @lc app=leetcode id=560 lang=python3
#
# [560] Subarray Sum Equals K
#

# @lc code=start
from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        prefixSum = defaultdict(int)  # To handle subarrays starting from index 0
        prefixSum[0] = 1
        currSum = 0
        noOfSubarrays = 0

        for num in nums:
            currSum += num
            if currSum - k in prefixSum:
                noOfSubarrays += prefixSum[currSum-k]

            prefixSum[currSum] += 1

        return noOfSubarrays

            

            


        
# @lc code=end

