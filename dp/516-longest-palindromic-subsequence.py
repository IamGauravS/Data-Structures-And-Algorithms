class Solution:
    
    def longestPalindromeSubseq(self, s: str) -> int:
        reversedStr = s[::-1]
        lenStr = len(s)

        dp = [[0] * (lenStr+1) for i in range(lenStr+1)]

        for i in range(lenStr):
            for j in range(lenStr):
                if s[i] == reversedStr[j]:
                    dp[i+1][j+1] = dp[i][j] + 1

                else:
                    dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])


        return dp[-1][-1]



class Solution:
    
    def longestPalindromeSubseq(self, s: str) -> int:
        dp = {}

        def dfs(i, j):
            if i < 0 or j == len(s):
                return 0
            if (i, j) in dp:
                return dp[(i,j)]
            
            if s[i] == s[j]:
                length = 1 if i == j else 2
                length += dfs(i-1, j+1)
                dp[(i,j)] = length

            else:
                length = max(dfs(i-1, j) dfs(i, j+1))
                dp[(i,j)] = length

            return dp[(i,j)]

            


        for i in range(len(s)):
            dfs(i, i)  ## odd length
            dfs(i, i+1)  ## even length


        return max(dp.values())



from functools import lru_cache

class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        @lru_cache(None)
        def dp(i, j):
            if i == j:
                return 1
            elif i > j:
                return 0
            if s[i] == s[j]:
                return 2 + dp(i + 1, j - 1)
            else:
                return max(dp(i + 1, j), dp(i, j - 1))
            
        s = list(s)
        return dp(0, len(s) - 1)
