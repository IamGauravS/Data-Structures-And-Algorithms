class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if matrix is None or len(matrix) < 1:
            return 0
        
        rows = len(matrix)
        cols = len(matrix[0])

        dp = [[0]*(cols+1) for _ in range(rows+1)]  # Adjust size of dp table

        maxSide = 0
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == '1':
                    dp[i+1][j+1] = min(dp[i][j], dp[i][j+1], dp[i+1][j]) + 1
                    maxSide = max(maxSide, dp[i+1][j+1])

        return maxSide * maxSide
