class Solution:
    def longestIncreasingPathHelper(self, i,j):
        if self.dp[i][j] != 0:
            return self.dp[i][j]

        delta = [(0,1), (1,0), (-1,0), (0,-1)]
        maxIncreasingPath = 0
        for dx,dy in delta:
            newi = i+dx
            newj = j+dy

            if 0 <= newi and newi < self.matrixHeight and 0 <= newj and newj < self.matrixWidth and self.matrix[i][j] < self.matrix[newi][newj]:
                maxIncreasingPath = max(maxIncreasingPath, self.longestIncreasingPathHelper(newi, newj))

        self.dp[i][j] = maxIncreasingPath+1
        self.maxIncreasingPathLength = max(self.maxIncreasingPathLength, self.dp[i][j])
        return self.dp[i][j]

    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        self.matrix = matrix
        self.matrixHeight = len(matrix)
        self.matrixWidth = len(matrix[0])
        self.maxIncreasingPathLength = 0

        self.dp = [[0 for i in range(self.matrixWidth)] for j in range(self.matrixHeight)]
        for i in range(self.matrixHeight):
            for j in range(self.matrixWidth):
                if self.dp[i][j] == 0:
                    self.dp[i][j] = self.longestIncreasingPathHelper(i,j)

        return self.maxIncreasingPathLength

