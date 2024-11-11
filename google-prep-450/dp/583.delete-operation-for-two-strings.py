#
# @lc app=leetcode id=583 lang=python3
#
# [583] Delete Operation for Two Strings
#

# @lc code=start
class Solution:
    def findLCSLen(self, s1 : str, s2 : str) -> int:
        """
        Calculates the length of the longest common subsequence between two strings using dynamic programming.

        Args:
            s1 (str): First input string.
            s2 (str): Second input string.

        Returns:
            int: Length of the longest common subsequence.
        """
        len1, len2 = len(s1), len(s2)
        dp = [0] * (len2 + 1)  # Using a 1D DP array to save space.

        for i in range(1, len1 + 1):
            prev = dp[:]
            for j in range(1, len2 + 1):
                # If characters match, increment from the diagonal
                if s1[i - 1] == s2[j - 1]:
                    dp[j] = prev[j - 1] + 1
                else:
                    # Otherwise, take the maximum of the previous row or column
                    dp[j] = max(prev[j], dp[j - 1])
                    
        return dp[len2]
    def minDistance(self, word1: str, word2: str) -> int:
        """
        This function returns minimum number of deletions required to make
        word1 and word2 same. 
        minimum number of deletions = word1-len(lcs) + word2-len(lcs)
        Args:
        word1 (str) : word 1
        word2 (str) : word 2

        Returns:
        minimumDeletions (int) : minimum deletions to make word1 and word2 same
        """

        ## if one of the string is empty then we need to delete all the elements
        ## from the other string
        if not word1:
            return len(word2)
        if not word2:
            return len(word1)
        if word1 == word2:
            return 0
        
        lcsLen = self.findLCSLen(word1, word2)

        minimumDeletions = len(word1) + len(word2) - 2*lcsLen
        return minimumDeletions
# @lc code=end

