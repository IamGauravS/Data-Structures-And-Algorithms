#
# @lc app=leetcode id=221 lang=python3
#
# [221] Maximal Square
#

# @lc code=start
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix or len(matrix[0]) == 0:
            return 0

        dp = [[0]*(len(matrix[0])+1) for _ in range(len(matrix)+1)]
        maxSize = 0
        for i in range(1, len(matrix)+1):
            for j in range(1, len(matrix[0])+1):
                if matrix[i-1][j-1] == "1":
                    dp[i][j] = 1 + min(dp[i-1][j-1], dp[i][j-1], dp[i-1][j])

                
            maxSize = max(maxSize, dp[i][j])


        return maxSize
        
# @lc code=end

