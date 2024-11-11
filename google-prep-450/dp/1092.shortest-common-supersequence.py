#
# @lc app=leetcode id=1092 lang=python3
#
# [1092] Shortest Common Supersequence 
#

# @lc code=start
class Solution:
    def findLCS(self, s1 : str, s2 : str) -> int:
        """
        Calculates the length of the longest common subsequence between two strings using dynamic programming.

        Args:
            s1 (str): First input string.
            s2 (str): Second input string.

        Returns:
            dp List[List[int]]: dp formed during lcs.
        """
        len1, len2 = len(s1), len(s2)
        dp = [[0] * (len2 + 1) for _ in range(len1+1)]  # Using a 1D DP array to save space.

        for i in range(1, len1 + 1):
            for j in range(1, len2 + 1):
                # If characters match, increment from the diagonal
                if s1[i - 1] == s2[j - 1]:
                    dp[i][j] = dp[i-1][j - 1] + 1
                else:
                    # Otherwise, take the maximum of the previous row or column
                    dp[i][j] = max(dp[i-1][j], dp[i][j - 1])
                    
        return dp
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        """
        This function returns the shortest string that has both str1 and str2
        as subsequences.
        """
        if not str1:
            return str2 
        if not str2:
            return str1 
        if str1 == str2:
            return str1 
        
        dp = self.findLCS(str1, str2)

        str1Ind = len(str1)
        str2Ind = len(str2)

        shortestSupersequence = ""

        while str1Ind > 0 and str2Ind > 0:
            if str1[str1Ind - 1] == str2[str2Ind - 1]:
                shortestSupersequence += str1[str1Ind - 1]
                str1Ind -= 1
                str2Ind -= 1
            ## if we move up we take char from str1
            elif dp[str1Ind - 1][str2Ind] > dp[str1Ind][str2Ind - 1]:
                shortestSupersequence += str1[str1Ind - 1]
                str1Ind -= 1 
            ## we move sideways we take char from str2
            else:
                shortestSupersequence += str2[str2Ind - 1]
                str2Ind -= 1
        ## add remaining characters from str1
        while str1Ind:
            shortestSupersequence += str1[str1Ind - 1]
            str1Ind -= 1 
        ## add remaining characters from str2
        while str2Ind:
            shortestSupersequence += str2[str2Ind - 1]
            str2Ind -= 1

        ## reverse
        return shortestSupersequence[::-1]

        
# @lc code=end

