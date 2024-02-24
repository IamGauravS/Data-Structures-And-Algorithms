def maximum_path(m, n):
    if m == n == 0:
        return 1 
    if m<0 or n<0:
        return 0
    return maximum_path(m-1,n) + maximum_path(m, n-1)


def maximum_path_dp(m,n):
    dp = [[-1 for j in range(n)] for _ in range(m)]

    for i in range(m):
        for j in range(n):
            # Base condition: If we are at the top-left corner, there is one way to reach it.
            if i == 0 and j == 0:
                dp[i][j] = 1
                continue
            
            # Initialize variables to store the number of ways from above and from the left.
            up = 0
            left = 0
            
            # Check if moving up is a valid option (not out of bounds).
            if i > 0:
                up = dp[i - 1][j]
            
            # Check if moving left is a valid option (not out of bounds).
            if j > 0:
                left = dp[i][j - 1]
            
            # Calculate and store the number of ways to reach the current cell.
            dp[i][j] = up + left
    
    # The bottom-right cell (m-1, n-1) now contains the total number of ways to reach there.
    return dp[m - 1][n - 1]