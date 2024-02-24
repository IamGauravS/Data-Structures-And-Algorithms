def find_max_reward(reward_arr, n):
    dp = [[-1]*3 for _ in range(n)]
    if n == 0:
        return 0

    dp[0] = reward_arr[0]

    for i in range(1, n):
        dp[i][0] = reward_arr[i][0] + max(dp[i-1][1], dp[i-1][2])
        dp[i][1] = reward_arr[i][1] + max(dp[i-1][0], dp[i-1][2])
        dp[i][2] = reward_arr[i][2] + max(dp[i-1][0], dp[i-1][1])

    return max(dp[n-1])

points = [[10, 40, 70],
          [20, 50, 80],
          [30, 60, 90]]

n = len(points)  # Get the number of days.
# Call the ninjaTraining function to find the maximum points.
print(find_max_reward(points, n))