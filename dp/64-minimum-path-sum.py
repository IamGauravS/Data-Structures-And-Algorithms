class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        gridHeight = len(grid)
        gridWidth = len(grid[0])

        dp = [[0] * gridWidth for j in range(gridHeight)]

        for i in range(gridHeight):
            if i == 0:
                dp[i][0] = grid[i][0]
            else:
                dp[i][0] = dp[i-1][0] + grid[i][0]

        for j in range(gridWidth):
            if j == 0:
                continue
            dp[0][j] = dp[0][j-1] + grid[0][j]

        for i in range(1, gridHeight):
            for j in range(1, gridWidth):
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]

        return dp[-1][-1]