#
# @lc app=leetcode id=115 lang=python3
#
# [115] Distinct Subsequences
#

# @lc code=start
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        lenS = len(s)
        lenT = len(t)

        # Initialize the dp array
        dp = [[0] * (lenT + 1) for _ in range(lenS + 1)]

        # Base case: An empty string is a subsequence of any string
        for i in range(lenS + 1):
            dp[i][0] = 1

        for i in range(1, lenS + 1):
            for j in range(1, lenT + 1):
                if s[i - 1] == t[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j]

        return dp[lenS][lenT]

class Solution:
    def numDistinctHelper(self, indexS, indexT):
        if indexT == len(self.target):
            return 1
        if indexS == len(self.source):
            return 0

        if self.dp[indexS][indexT] != -1:
            return self.dp[indexS][indexT]
        
        noOfWays = self.numDistinctHelper(indexS+1, indexT)

        if self.source[indexS] == self.target[indexT]:
            noOfWays += self.numDistinctHelper(indexS+1, indexT+1) 

        self.dp[indexS][indexT] = noOfWays

        return noOfWays

    def numDistinct(self, s: str, t: str) -> int:
        self.source = s
        self.target = t
        self.dp = [[-1]*len(t) for _ in range(len(s))]

        return self.numDistinctHelper(0, 0)
                
        
# @lc code=end

