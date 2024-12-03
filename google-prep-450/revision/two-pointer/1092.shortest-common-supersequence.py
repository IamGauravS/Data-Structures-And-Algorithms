#
# @lc app=leetcode id=1092 lang=python3
#
# [1092] Shortest Common Supersequence 
#

# @lc code=start
class Solution:
    def lcs(self, str1, str2):
        # Compute the Longest Common Subsequence (LCS) DP table
        dp = [[0] * (len(str2) + 1) for _ in range(len(str1) + 1)]

        for i in range(1, len(str1) + 1):
            for j in range(1, len(str2) + 1):
                if str1[i - 1] == str2[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        return dp

    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        # Get the LCS DP table
        dp = self.lcs(str1, str2)

        # Indices for traversing str1 and str2
        str1Idx = len(str1)
        str2Idx = len(str2)

        # Result string for the SCS
        output = []

        # Backtrack to construct the SCS
        while str1Idx > 0 and str2Idx > 0:
            if str1[str1Idx - 1] == str2[str2Idx - 1]:
                # Characters match, add to output
                output.append(str1[str1Idx - 1])
                str1Idx -= 1
                str2Idx -= 1
            else:
                # Characters do not match, choose the one with the larger LCS value
                if dp[str1Idx - 1][str2Idx] >= dp[str1Idx][str2Idx - 1]:
                    output.append(str1[str1Idx - 1])
                    str1Idx -= 1
                else:
                    output.append(str2[str2Idx - 1])
                    str2Idx -= 1

        # Add remaining characters from str1 or str2
        while str1Idx > 0:
            output.append(str1[str1Idx - 1])
            str1Idx -= 1
        while str2Idx > 0:
            output.append(str2[str2Idx - 1])
            str2Idx -= 1

        # Reverse the result as it was constructed backwards
        return "".join(reversed(output))

        
# @lc code=end

