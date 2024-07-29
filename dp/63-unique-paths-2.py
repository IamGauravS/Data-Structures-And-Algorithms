class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid[0])
        n = len(obstacleGrid)

        dp = [[0 for i in range(m)] for j in range(n)]

        for i in range(n):
            if obstacleGrid[i][0] != 1:
                if i == 0:
                    dp[i][0] = 1
                else:        
                    dp[i][0] = dp[i-1][0] 

        for j in range(m):
            if obstacleGrid[0][j] != 1:
                if j == 0:
                    continue

                dp[0][j] = dp[0][j-1] 

        for i in range(1, n):
            for j in range(1, m):
                if obstacleGrid[i][j] != 1:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]

        return dp[-1][-1]