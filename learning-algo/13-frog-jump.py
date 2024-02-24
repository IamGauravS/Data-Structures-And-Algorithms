def frog_jump(arr, n):
    if n ==0:
        return 0
    
    dp = [-1]*(n+1)
    dp[0] = 0
    dp[1] = abs(arr[1] - arr[0])
    
    for i in range(2, n):
        single_jump = dp[i-1] + abs(arr[i] - arr[i-1])
        double_jump = dp[i-2] + abs(arr[i] - arr[i-2])

        dp[i] = min(single_jump, double_jump)

    return dp[n-1]



height = [30, 10, 60, 10, 60, 50]
print(frog_jump(height, len(height)))