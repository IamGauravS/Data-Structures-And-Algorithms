def maximum_falling_path(arr,m,n):
    dp = [[-1 for i in range(m)] for j in range(n)]

    dp[n-1] = arr[n-1].copy()

    for i in range(n-2,-1,-1):
        for j in range(m):
            bottom = dp[i-1][j]
            left_diagonal = -1
            if j-1 >=0:
                left_diagonal = dp[i-1][j-1]
            right_diagonal = -1
            if j+1 < m:
                right_diagonal = dp[i-1][j+1]

            dp[i][j] = max(bottom, left_diagonal, right_diagonal) + arr[i][j]

    return max(dp[0])

