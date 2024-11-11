#
# @lc app=leetcode id=516 lang=python3
#
# [516] Longest Palindromic Subsequence
#

# @lc code=start
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        """
        This function returns the length of the longest subsequence
        in a string. It uses bottoms up dynamic programming approach to achieve this.
        We take the string and reverse it and then try to find the longest common substring
        between both. We can further optimise this function by using 1-D
        DP since we just need the previous row but for the sake of clearity we are using 2-D dp

        Args:
        s (str)  -> input string
        Returns:
        longestSubsequenceLength (int) -> length of the longest palindromic subsequence
        """
        
        strLen = len(s)
        revStr = s[::-1] ## reverse the string
        ## intialise the dp array

        dp = [[0]*(strLen+1) for _ in range(strLen+1)]

        for i in range(1, strLen+1):
            for j in range(1, strLen+1):
                ## we take max of either (i-1,j) or (j,i-1)
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

                ## if both the characters are equal then we have an 
                ## extra option to consider both
                if s[i-1] == revStr[j-1]:
                    dp[i][j] = max(dp[i][j], 1 + dp[i-1][j-1])

        longestSubsequenceLength = dp[strLen][strLen]
        return longestSubsequenceLength


# @lc code=end

