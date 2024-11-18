#
# @lc app=leetcode id=1043 lang=python3
#
# [1043] Partition Array for Maximum Sum
#

# @lc code=start
class Solution:
    def maxSumAfterPartitioningHelper(self, start, end):
        if start >= end:
            return 0
        
        if (start, end) in self.dp:
            return self.dp[(start, end)]
        
        maxSum = -float('inf')

        for ind in range(start, min(end, start + self.k)):
            leftPartition = self.arr[start:ind+1]
            leftSumMax = max(leftPartition)
            leftSum  = leftSumMax * (ind - start + 1)
            rightSum = self.maxSumAfterPartitioningHelper(ind + 1, end)
            currSum = leftSum + rightSum
            maxSum = max(currSum, maxSum)

        self.dp[(start, end)] = maxSum
        return maxSum

    def maxSumAfterPartitioningMemo(self, arr: List[int], k: int) -> int:
        self.k = k
        self.arr = arr
        self.dp = {}
        return self.maxSumAfterPartitioningHelper(0, len(arr))

    
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n = len(arr)
        dp = [0] * (n + 1)  # `dp[i]` represents the max sum from `arr[0]` to `arr[i-1]`

        for i in range(1, n + 1):  # Iterate over the array from 1 to n (1-based indexing)
            maxElement = 0
            for j in range(1, min(k, i) + 1):  # Check partitions of size 1 to k
                maxElement = max(maxElement, arr[i - j])  # Maximum element in the current partition
                dp[i] = max(dp[i], dp[i - j] + maxElement * j)  # Update the max sum at index `i`

        return dp[n]  # Return the max sum for the entire array

        
# @lc code=end

