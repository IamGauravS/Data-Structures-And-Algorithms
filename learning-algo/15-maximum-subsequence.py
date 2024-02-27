def max_subseq(arr,n):
    dp = [-1]*(n+1) 

    dp[0] = 0
    dp[1] = arr[0]

    for i in range(2, n+1):
        max_rece = dp[i-1]
        max_one_jump = dp[i-2] + arr[i-1]
        dp[i] = max(max_rece, max_one_jump)

    return dp[n]

