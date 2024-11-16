from typing import List


from bisect import bisect_left

class Solution:
    def lengthOfLIS(self, nums):
        """
        Helper function to calculate the LIS using Binary Search.
        """
        lis = []
        dp = [0] * len(nums)  # dp[i] stores the length of LIS ending at i
        
        for i, num in enumerate(nums):
            pos = bisect_left(lis, num)  # Find the position to replace or append
            if pos == len(lis):
                lis.append(num)  # Extend LIS
            else:
                lis[pos] = num  # Replace element at 'pos'
            dp[i] = pos + 1
        
        return dp

    def LongestBitonicSequence(self, n, nums):
        # LIS from the front
        dpIncreasing = self.lengthOfLIS(nums)

        # LIS from the back (LDS)
        dpDecreasing = self.lengthOfLIS(nums[::-1])[::-1]

        # Combine LIS and LDS to find the longest bitonic sequence
        maxBitonic = 0
        for i in range(n):
            if dpIncreasing[i] != 1 and dpDecreasing[i] != 1:
                maxBitonic = max(maxBitonic, dpIncreasing[i] + dpDecreasing[i] - 1)

        return maxBitonic
