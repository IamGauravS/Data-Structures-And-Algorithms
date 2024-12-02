#
# @lc app=leetcode id=2035 lang=python3
#
# [2035] Partition Array Into Two Arrays to Minimize Sum Difference
#

# @lc code=start
from typing import List
from itertools import combinations
import bisect

class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        n = len(nums) // 2
        total_sum = sum(nums)
        target = total_sum // 2

        # Split into two halves
        left, right = nums[:n], nums[n:]

        # Function to get all possible subset sums for a given list of numbers
        def get_subset_sums(arr):
            subset_sums = [[] for _ in range(len(arr) + 1)]
            for k in range(len(arr) + 1):
                for comb in combinations(arr, k):
                    subset_sums[k].append(sum(comb))
            return subset_sums

        # Get subset sums for left and right halves
        left_sums = get_subset_sums(left)
        right_sums = get_subset_sums(right)

        # Sort the subset sums of each size for binary searching
        for sums in right_sums:
            sums.sort()

        # Initialize the minimum difference
        min_diff = float('inf')

        # For each possible number of elements chosen from the left half
        for k in range(n + 1):
            for left_sum in left_sums[k]:
                # We want the closest sum in right_sums[n - k] to balance to `target`
                closest_sum = target - left_sum

                # Binary search to find the closest sum in right half
                idx = bisect.bisect_left(right_sums[n - k], closest_sum)

                # Check the two closest candidates in right_sums[n - k] if they exist
                if idx < len(right_sums[n - k]):
                    right_sum = right_sums[n - k][idx]
                    diff = abs((left_sum + right_sum) * 2 - total_sum)
                    min_diff = min(min_diff, diff)

                if idx > 0:
                    right_sum = right_sums[n - k][idx - 1]
                    diff = abs((left_sum + right_sum) * 2 - total_sum)
                    min_diff = min(min_diff, diff)

        return min_diff
        
# @lc code=end

