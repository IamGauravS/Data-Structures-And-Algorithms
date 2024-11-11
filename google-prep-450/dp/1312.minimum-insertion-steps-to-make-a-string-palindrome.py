#
# @lc app=leetcode id=1312 lang=python3
#
# [1312] Minimum Insertion Steps to Make a String Palindrome
#

# @lc code=start
from typing import List

class Solution:
    def longestCommonSubsequence(self, s1: str, s2: str) -> int:
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

    def minInsertions(self, s: str) -> int:
        """
        Computes the minimum number of insertions required to make a string a palindrome.

        This is achieved by finding the length of the longest palindromic subsequence (LPS)
        and then calculating the difference between the string length and the LPS length.

        Args:
            s (str): Input string.

        Returns:
            int: Minimum number of insertions required to make the string a palindrome.
        """
        if not s:
            return 0
        
        # Find the longest palindromic subsequence length by comparing the string with its reverse
        longest_palindromic_subseq_len = self.longestCommonSubsequence(s, s[::-1])
        
        # Minimum insertions needed is the difference between the string length and LPS length
        return len(s) - longest_palindromic_subseq_len


        

        
# @lc code=end

