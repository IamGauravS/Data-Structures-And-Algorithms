class Solution:
    def longestCommonSubstr(self, s1, s2):
        # code here
        dp = [[0]*(len(s1)+1) for _ in range(len(s2)+1)]
        
        maxLen = 0
        for i in range(1, len(s2)+1):
            for j in range(1, len(s1)+1):
                if s1[j-1] == s2[i-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                    maxLen = max(maxLen, dp[i][j])
                else:
                    dp[i][j] = 0
                    
        return maxLen