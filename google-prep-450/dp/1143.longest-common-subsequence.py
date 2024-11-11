#
# @lc app=leetcode id=1143 lang=python3
#
# [1143] Longest Common Subsequence
#

# @lc code=start
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        len1 = len(text1)
        len2 = len(text2)

        dp  = [[0]*(len2+1) for _ in range(len1+1)]

        for i in range(1, len1+1):
            for j in range(1, len2+1):
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

                if text1[i-1] == text2[j-1]:
                    dp[i][j] = max(dp[i][j], dp[i-1][j-1] + 1)


        return dp[len1][len2]
        
# @lc code=end

