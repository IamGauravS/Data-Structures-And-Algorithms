class Solution:
    def matrixMultiplicationHelper(self, i, j):
        # Base case: only one matrix
        if i == j:
            return 0
        
        # Return the result if it is already computed
        if (i, j) in self.dp:
            return self.dp[(i, j)]
        
        # Initialize the minimum number of multiplications to infinity
        mini = float('inf')
        
        # Try all possible positions to split the matrices
        for m in range(i, j):
            # Calculate the number of multiplications for the current split
            steps = (self.arr[i-1] * self.arr[m] * self.arr[j] +
                     self.matrixMultiplicationHelper(i, m) +
                     self.matrixMultiplicationHelper(m+1, j))
            # Update the minimum number of multiplications
            mini = min(steps, mini)

        # Store the result in the dp dictionary
        self.dp[(i, j)] = mini
        return self.dp[(i, j)]
    
    def matrixMultiplicationHelperTabulation(self, arr):
        n = len(arr)
        # Initialize the dp table with 0s
        dp = [[0 for _ in range(n)] for _ in range(n)]

        # l is the chain length
        for l in range(2, n):  # l starts from 2 because we need at least two matrices to multiply
            for i in range(1, n - l + 1):
                j = i + l - 1
                dp[i][j] = float('inf')
                for k in range(i, j):
                    # Calculate the cost of multiplying the matrices from i to j
                    cost = dp[i][k] + dp[k + 1][j] + arr[i - 1] * arr[k] * arr[j]
                    # Update the dp table with the minimum cost
                    dp[i][j] = min(dp[i][j], cost)

        # The result is stored in dp[1][n-1]
        return dp[1][n - 1]


    def matrixMultiplication(self, arr):
        # Initialize the dp dictionary and the array of dimensions
        self.dp = {}
        self.arr = arr
        # Call the helper function with the initial indices
        return self.matrixMultiplicationHelper(1, len(arr)-1)

# Example usage:
solution = Solution()
print(solution.matrixMultiplication([1, 2, 3, 4]))  # Output: 18
    
