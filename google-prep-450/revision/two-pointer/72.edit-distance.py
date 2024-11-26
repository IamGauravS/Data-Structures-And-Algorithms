#
# @lc app=leetcode id=72 lang=python3
#
# [72] Edit Distance
#

# @lc code=start
class Solution:
    def minDistanceHelper(self, word1, word2, index1, index2):
        
        if len(word1) == index1:
            return len(word2) - index2
        if len(word2) == index2:
            return len(word1) - index1

        if (index1, index2) in self.memDict:
            return self.memDict[(index1, index2)]

        if word1[index1] == word2[index2]:
            self.memDict[(index1, index2)] =  self.minDistanceHelper(word1, word2, index1+1, index2+1)
        
        else:
            ## insert
            insert = self.minDistanceHelper(word1, word2, index1, index2 + 1)
            ## delete
            delete = self.minDistanceHelper(word1, word2, index1+1, index2)
            ## replace
            replace = self.minDistanceHelper(word1, word2, index1+1, index2+1)

            self.memDict[(index1, index2)] =  1 + min(insert, delete, replace)

        return self.memDict[(index1, index2)]

    def minDistance(self, word1: str, word2: str) -> int:
        
        dp = [[0]*(len(word1)+1) for _ in range(len(word2)+1)]

        for i in range(len(word2)+1):
            dp[i][len(word1)] = len(word2) - i

        for j in range(len(word1)+1):
            dp[len(word2)][j] = len(word1) - j

        for i in range(len(word2)-1, -1, -1):
            for j in range(len(word1)-1, -1, -1):
                if word2[i] == word1[j]:
                    dp[i][j] = dp[i+1][j+1]
                else:
                    dp[i][j] = 1 + min(dp[i][j+1], dp[i+1][j], dp[i+1][j+1])

        return dp[0][0]

        
        
        
# @lc code=end

