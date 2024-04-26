class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        self.grid = grid

        
        self.width = len(grid[0])
        self.height = len(grid)
        self.dp = [[float('inf') for i in range(self.width)] for j in range(self.height)]

        for i in range(self.width):
            self.dp[-1][i] = self.grid[-1][i]

        for i in range(self.height-2, -1, -1):
            for j in range(self.height-1, -1, -1):
                for k in range(self.height-1, -1, -1):
                    if k != j:
                        self.dp[i][j] = min(self.dp[i][j], self.dp[i+1][k])

                self.dp[i][j] += self.grid[i][j]



        return min(self.dp[0]) 