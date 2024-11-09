
import sys

# Recursive function to find the maximum chocolates collected
def maxChocoUtil(i, j1, j2, n, m, grid, dp):
    # Base cases:
    # - If either of the indices is out of bounds, return a large negative value
    # - If we're at the last row, return the sum of chocolates in the two selected columns
    if j1 < 0 or j1 >= m or j2 < 0 or j2 >= m:
        return int(-1e9)
    if i == n - 1:
        if j1 == j2:
            return grid[i][j1]
        else:
            return grid[i][j1] + grid[i][j2]
    
    # If the result for these indices has already been computed, return it
    if dp[i][j1][j2] != -1:
        return dp[i][j1][j2]
    
    # Initialize the maximum chocolates collected to a large negative value
    maxi = -sys.maxsize
    
    # Iterate through the adjacent cells in the next row
    for di in range(-1, 2):
        for dj in range(-1, 2):
            ans = 0
            if j1 == j2:
                ans = grid[i][j1] + maxChocoUtil(i + 1, j1 + di, j2 + dj, n, m, grid, dp)
            else:
                ans = grid[i][j1] + grid[i][j2] + maxChocoUtil(i + 1, j1 + di, j2 + dj, n, m, grid, dp)
            maxi = max(maxi, ans)
    
    # Store the maximum chocolates collected in the memoization table
    dp[i][j1][j2] = maxi
    return maxi

# Function to find the maximum chocolates collected
def maximumChocolates(n, m, grid):
    # Initialize a memoization table with -1 values
    dp = [[[-1 for j in range(m)] for i in range(m)] for k in range(n)]
    
    # Start the recursion from the first row, columns 0 and m-1
    return maxChocoUtil(0, 0, m - 1, n, m, grid, dp)





import sys

# Function to find the maximum chocolates collected
def maximumChocolates(n, m, grid):
    # Initialize a 3D memoization table dp with zeros
    dp = [[[0 for _ in range(m)] for _ in range(m)] for _ in range(n)]

    # Initialize the values for the last row of dp based on grid values
    for j1 in range(m):
        for j2 in range(m):
            if j1 == j2:
                dp[n - 1][j1][j2] = grid[n - 1][j1]
            else:
                dp[n - 1][j1][j2] = grid[n - 1][j1] + grid[n - 1][j2]

    # Iterate through rows from the second-to-last row to the first row
    for i in range(n - 2, -1, -1):
        for j1 in range(m):
            for j2 in range(m):
                maxi = -sys.maxsize

                # Try out 9 possible options by changing the indices
                for di in range(-1, 2):
                    for dj in range(-1, 2):
                        ans = 0
                        if j1 == j2:
                            ans = grid[i][j1]
                        else:
                            ans = grid[i][j1] + grid[i][j2]

                        if ((j1 + di < 0 or j1 + di >= m) or (j2 + dj < 0 or j2 + dj >= m)):
                            ans += int(-1e9)  # A large negative value if out of bounds
                        else:
                            ans += dp[i + 1][j1 + di][j2 + dj]  # Add the value from the next row

                        maxi = max(ans, maxi)

                # Store the maximum chocolates collected in the memoization table
                dp[i][j1][j2] = maxi

    # Return the maximum chocolates collected in the top row and the last column
    return dp[0][0][m - 1]

def main():
    # Define the input matrix and its dimensions
    matrix = [[2, 3, 1, 2], [3, 4, 2, 2], [5, 6, 3, 5]]
    n = len(matrix)
    m = len(matrix[0])

    # Call the maximumChocolates function and print the result
    print(maximumChocolates(n, m, matrix))

if __name__ == '__main__':
    main()

