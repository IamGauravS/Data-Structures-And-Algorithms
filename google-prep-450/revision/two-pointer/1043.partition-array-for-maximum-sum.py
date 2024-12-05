#
# @lc app=leetcode id=1043 lang=python3
#
# [1043] Partition Array for Maximum Sum
#

# @lc code=start
class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n = len(arr)
        dp = [0] * (n + 1)  # DP array with one extra element for boundary condition

        # Fill the DP array from the end to the start
        for i in range(n - 1, -1, -1):
            maxValue = -float('inf')
            maxSum = -float('inf')

            # Iterate over partition sizes
            for j in range(i, min(i + k, n)):
                maxValue = max(maxValue, arr[j])  # Keep track of max in the current partition
                partitionSum = maxValue * (j - i + 1) + dp[j + 1]  # Current partition + next subproblem
                maxSum = max(maxSum, partitionSum)

            dp[i] = maxSum  # Store the maximum sum for starting at index i

        return dp[0]

        
# @lc code=end

