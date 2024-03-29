class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        len1 = len(text1)
        len2 = len(text2)
        
        dp = [[0 for i in range(len1+1)] for j in range(len2+1)]
        
        for i in range(1, len2+1):
            for j in range(1, len1+1):
                
                if text2[i-1] == text1[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                    
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
                    
                    
        return dp[len2][len1]