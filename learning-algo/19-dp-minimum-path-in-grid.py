import sys
def minimum_path_sum(arr,m,n):
    dp = [[sys.maxsize for i in range(m+1)] for _ in range(n+1)]
    dp[0][0] = arr[0][0]

    for i in range(1, m+1):
        dp[0][i] = arr[0][i] + dp[0][i-1]

    for j in range(1, n+1):
        dp[j][0] = arr[j][0] + dp[j-1][0]

    for i in range(1, n+1):
        for j in range(1, m+1):
            dp[i][j] = arr[i][j] + min(dp[i-1][j], dp[i][j-1])

    return dp[n][m]