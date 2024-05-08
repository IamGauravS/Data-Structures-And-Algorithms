class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        height = len(matrix)
        width = len(matrix[0])

        dp = [[0]*width for i in range(height)]

        for i in range(width):
            dp[0][i] = matrix[0][i]

        for i in range(1, height):
            for j in range(width):
                minPrev = min(dp[i-1][j], dp[i-1][j-1] if j-1 >= 0 else float('inf'), dp[i-1][j+1] if j+1 < width else float('inf'))

                dp[i][j] = minPrev + matrix[i][j]

        return min(dp[-1])