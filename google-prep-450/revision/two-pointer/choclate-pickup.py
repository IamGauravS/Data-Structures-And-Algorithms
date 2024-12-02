class Solution:
    def solveHelper(self, i, j1, j2, grid):
        if i == len(grid) - 1:
            if j1 != j2:
                return grid[i][j1] + grid[i][j2]
            else:
                return grid[i][j1]
        
        if (i, j1, j2) in self.memDict:
            return self.memDict[(i, j1, j2)]
            
        delta = [-1, 0, 1]
        self.memDict[(i, j1, j2)] = -float('inf')
        for d1 in delta:
            for d2 in delta:
                newj1 = j1 + d1
                newj2 = j2 + d2
                
                if 0 <= newj1 < len(grid[0]) and 0 <= newj2 < len(grid[0]):
                        self.memDict[(i, j1, j2)] = max(self.memDict[(i, j1, j2)], self.solveHelper(i+1, newj1, newj2, grid))
                        
        if j1 != j2:
            self.memDict[(i, j1, j2)] += (grid[i][j1] + grid[i][j2])
        else:
            self.memDict[(i, j1, j2)] += grid[i][j1]
            
        return self.memDict[(i, j1, j2)]
        
                
    def solve(self, n, m, grid):
        # Initialize a 3D DP table with negative infinity
        dp = [[[-float('inf')] * m for _ in range(m)] for _ in range(n)]
        
        # Base case: Fill the last row
        for j1 in range(m):
            for j2 in range(m):
                if j1 != j2:
                    dp[n - 1][j1][j2] = grid[n - 1][j1] + grid[n - 1][j2]
                else:
                    dp[n - 1][j1][j2] = grid[n - 1][j1]
        
        # Directions for delta (movement)
        delta = [-1, 0, 1]
        
        # Fill the DP table from bottom to top
        for i in range(n - 2, -1, -1):
            for j1 in range(m):
                for j2 in range(m):
                    for d1 in delta:
                        for d2 in delta:
                            newj1 = j1 + d1
                            newj2 = j2 + d2
                            
                            # Check bounds
                            if 0 <= newj1 < m and 0 <= newj2 < m:
                                dp[i][j1][j2] = max(
                                    dp[i][j1][j2],
                                    dp[i + 1][newj1][newj2]
                                )
                    
                    # Add the current grid values
                    if j1 != j2:
                        dp[i][j1][j2] += grid[i][j1] + grid[i][j2]
                    else:
                        dp[i][j1][j2] += grid[i][j1]
        
        # Return the maximum chocolates collected starting from (0,0) and (0,m-1)
        return dp[0][0][m - 1]
