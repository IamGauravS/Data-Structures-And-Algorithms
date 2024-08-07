class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        lenText1 = len(text1)
        lenText2 = len(text2)

        dp = [[0 for i in range(lenText2+1)] for j in range(lenText1+1)]

        for i in range(lenText1-1, -1, -1):
            for j in range(lenText2-1, -1, -1):
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i+1][j+1]

                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j+1])

        return dp[0][0]


## we can further optimise this since we only need two rows